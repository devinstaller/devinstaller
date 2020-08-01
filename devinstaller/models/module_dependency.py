"""Module dependency graph and other stuffs
"""
from typing import Any, Dict, List, Set

from typeguard import typechecked

from devinstaller.exceptions import ModuleInstallationFailed, SpecificationError
from devinstaller.models.app_module import AppModule
from devinstaller.models.common_models import TypeAnyModule, TypeCommonModule
from devinstaller.models.file_module import FileModule
from devinstaller.models.folder_module import FolderModule
from devinstaller.models.group_module import GroupModule
from devinstaller.models.link_module import LinkModule
from devinstaller.models.phony_module import PhonyModule
from devinstaller.models.platform_block import PlatformBlock
from devinstaller.utilities import UserInteract, remove_key


class ModuleDependency:
    """Module dependency class

    Args:
        graph: The dependency graph
        orphan_modules: The "list" of modules not used by any other modules
    """

    @typechecked
    def __init__(
        self, module_list: List[TypeCommonModule], platform_object: PlatformBlock
    ) -> None:
        """Create dependency graph
        """
        self.graph: Dict[str, TypeAnyModule] = {}
        self.orphan_modules: Set[str] = set()
        module_classes: Dict[str, Any] = {
            "app": AppModule,
            "file": FileModule,
            "folder": FolderModule,
            "link": LinkModule,
            "group": GroupModule,
            "phony": PhonyModule,
        }
        for module_object in module_list:
            if check_platform_compatibility(platform_object, module_object):
                module_type = module_object["module_type"]
                module_object = remove_key(module_object, "supported_platforms")
                module_object = remove_key(module_object, "module_type")
                new_module = module_classes[module_type](**module_object)
                assert new_module.alias is not None
                codename = new_module.alias
                if codename in self.graph:
                    self.graph[codename] = select_module(
                        old_module=self.graph[codename], new_module=new_module
                    )
                else:
                    self.graph[codename] = new_module

    def uninstall_orphan_modules(self) -> None:
        """Uninstall orphan modules

        Modules which are not used by any other modules
        """
        for module_name in self.orphan_modules:
            self.graph[module_name].uninstall()

    def module_list(self) -> List[TypeAnyModule]:
        """Returns the list of all the modules that have been initialized by the Module dependency
        """
        return list(self.graph.values())

    def install(self, requirement_list: List[str]) -> None:
        """Install all the modules you want

        The `traverse` function can install only one module and its dependencies, but
        this method can install more than one module.

        It is a wrapper around the `traverse` method.

        This method takes in a list as an argument and installs it.
        """
        for module_name in requirement_list:
            self.traverse(module_name)

    @typechecked
    def traverse(self, module_name: str) -> None:
        """Reverse DFS logic for traversing dependencies.

        Basically it installs all the dependencies first then app.

        Args:
            module_map: The module map of current platform
            module_name: The name of the module to traverse
            orphan_list: The list of modules which are not used by any other modules

        Raises:
            SpecificationError
                if one of your module requires but the required module itself is not present
        """
        try:
            module = self.graph[module_name]
        except KeyError:
            raise SpecificationError(
                error=module_name,
                error_code="S100",
                message="The name of the module given by you didn't match with the codenames of the modules",
            )
        if module.status is not None:
            if module.alias in self.orphan_modules:
                self.orphan_modules.remove(module.alias)
            return None
        module.status = "in progress"
        self.traverse_requires(module_name)
        self.traverse_optionals(module_name)
        self.traverse_install(module_name)
        return None

    @typechecked
    def traverse_requires(self, module_name: str) -> None:
        """Recusively traverse the requires field of the module for its dependencies

        Args:
            module_map: The module map for the current platform
            module: The module you want to traverse
            orphan_list: The list of modules not used by any other modules

        Returns:
            The updated orphan_list
        """
        module = self.graph[module_name]
        if isinstance(module, PhonyModule):
            return None
        if module.requires is None:
            return None
        for index, child_name in enumerate(module.requires):
            self.traverse(child_name)
            if self.graph[child_name].status == "failed":
                print(
                    f"The module {child_name} in the requires of {module.alias} has failed"
                )
                module.status = "failed"
                self.orphan_modules.update(module.requires[:index])
                return None
        return None

    @typechecked
    def traverse_optionals(self, module_name: str) -> None:
        """Recusively traverse the optionals field of the module for its dependencies

        Args:
            module_map: The module map for the current platform
            module: The module you want to traverse
            orphan_list: The list of modules not used by any other modules

        Returns:
            The updated orphan_list
        """
        module = self.graph[module_name]
        if isinstance(module, PhonyModule):
            return None
        if module.optionals is None:
            return None
        for child_name in module.optionals:
            self.traverse(child_name)
            if self.graph[child_name].status == "failed":
                print(
                    f"The module {child_name} in the optionals of {module.alias} has failed, "
                    "but the installation for remaining modules will continue"
                )
        return None

    @typechecked
    def traverse_install(self, module_name: str) -> None:
        """The main function which handles the installation as well as its final installation
        status
        """
        module = self.graph[module_name]
        try:
            module.install()
            module.status = "success"
            return None
        except ModuleInstallationFailed:
            print(
                f"The installation for the module: {module.alias} failed. "
                "And all the instructions has been rolled back."
            )
            module.status = "failed"
            if isinstance(module, PhonyModule):
                return None
            if module.requires is not None:
                self.orphan_modules.update(module.requires)
            if module.optionals is not None:
                self.orphan_modules.update(module.optionals)


@typechecked
def check_platform_compatibility(
    platform_object: PlatformBlock, module: TypeCommonModule
) -> bool:
    """Checks if the given module is compatible with the current platform.

    Steps:
        1. Checks if the user has provided `supported_platforms` key-value pair
           in the module object. If it is NOT provided then it is assumed that this specific
           module is compatible with all platforms and returns True.
        2. Checks if the platform object is a "mock" platform object or not.
           If the user didn't provided platforms block in the spec a "mock"
           platform object as placeholder is generated. So it checks whether is
           this the mock object or not. If it is then `SpecificationError` is raised.
        3. Checks if the platform name is supported by the module. If yes then returns True.
        4. Nothing else then returns False

    Args:
        platform_object: The current platform object
        module: The module object

    Returns:
        True if compatible else False

    Raises:
        SpecificationError
            with error code :ref:`error-code-S100`
    """
    if "supported_platforms" not in module:
        return True
    if platform_object.codename == "MOCK":
        raise SpecificationError(
            module["name"], "S100", "You are missing a platform object"
        )
    if platform_object.codename in module["supported_platforms"]:
        return True
    return False


@typechecked
def select_module(
    old_module: TypeAnyModule, new_module: TypeAnyModule
) -> TypeAnyModule:
    """Sometimes the spec may have already declared two modules with same codename and for the same platform

    In such cases we ask the user to select which one to use for the current session.

    Only one can be used for the current session.

    Please note that the spec allows for multiple modules with same codename and usually they are for different platforms
    but other wise you need to select one. You can't use multiple modules with same codename in the same session.

    Args:
        old_module: The old module which is already present in the `module_map`
        new_module: The new module which happens to share the same codename of the `old_module`

    Returns:
        The selected module
    """
    print("Oops, looks like your spec has two modules with the same codename.")
    print("But for the current session I can use only one.")
    print("This is the first module")
    print(old_module)
    print("And this is the second module")
    print(new_module)
    title = "Do you mind selecting one?"
    choices = ["First one", "Second one"]
    selection = UserInteract.select(title, choices)
    if selection == "First one":
        return old_module
    return new_module
