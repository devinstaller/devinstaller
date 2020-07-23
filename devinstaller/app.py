"""The main module which is used by CLI and Library
"""
from typing import Any, Dict, List, Optional, Set

from typeguard import typechecked

from devinstaller import exceptions as e
from devinstaller import file_handler as f
from devinstaller import models as m
from devinstaller import schema as s
from devinstaller import utilities as u


@typechecked
def install(
    file_path: Optional[str] = None,
    spec_object: Optional[Dict[Any, Any]] = None,
    platform_codename: Optional[str] = None,
    requirements_list: Optional[List[str]] = None,
) -> None:
    """Install the default preset and the modules which it requires.

    There are two ways this function works.

    1. Passing the file_path (Default method for the CLI usage)
    2. Passing the spec_object

    If you pass the file path then it takes the precedance and the file is read
    and the object is loaded.

    If not then it checks for the schema_object and if it is not present then
    `ImplementationError` is raised.

    And in either case the object will be validated before further processing.

    Args:
        file_path: Takes in path to the spec file
        spec_object: Takes in the full spec file as a python dict
        platform_codename: The name of the platform
        module: The name of the module to installed

    raises:
        ImplementationError
            with error code :ref:`error-code-D100`
    """
    if file_path is not None:
        schema_object: Dict[Any, Any] = f.read_file_and_parse(file_path=file_path)
    elif spec_object is not None:
        schema_object = spec_object
    else:
        raise e.DevinstallerError("Schema object not found", "D100")
    validated_schema_object = s.get_validated_document(schema_object)
    platform_object = s.get_platform_object(validated_schema_object, platform_codename)
    dependency_graph = m.ModuleDependency(
        module_list=validated_schema_object["modules"], platform_object=platform_object
    )
    if requirements_list is None:
        requirement_list = ask_user_for_the_requirement_list(
            dependency_graph.module_list()
        )
    dependency_graph.install(requirement_list)
    orphan_modules_names = dependency_graph.orphan_modules
    if orphan_modules_names != set():
        if ask_user_for_uninstalling_orphan_modules(orphan_modules_names):
            dependency_graph.uninstall_orphan_modules()


@typechecked
def ask_user_for_the_requirement_list(
    module_objects: List[m.TypeAnyModule],
) -> List[str]:
    """Ask the user for which modules to be installed

    Args:
        module_objects: List of all the modules you want to display to the user

    Returns:
        List of the objects of all the modules to be installed.
    """
    print("Hey... You haven't selected which module to be installed")
    title = "Do you mind selected a few for me?"
    choices = {str(mod): mod for mod in module_objects}
    selections = u.ask_user_for_multi_select(title, choices=list(choices.keys()))
    data: List[str] = []
    for _s in selections:
        _m = choices[_s]
        assert _m.alias is not None
        data.append(_m.alias)
    return data


def show(file_name: str) -> None:
    """TODO
    """
    # TODO Write the function to show all the modules defined in the spec file


@typechecked
def ask_user_for_uninstalling_orphan_modules(orphan_list: Set[str]) -> bool:
    """Asks user for confirmation for the uninstallation of the orphan modules.

    Args:
        orphan_list: The "list" of modules which are not used by any other modules
    """
    print(
        "Because of failed installation of some modules, there are some"
        "modules which are installed but not required by any other modules"
    )
    orphan_module_names = ", ".join(name for name in orphan_list)
    print(f"These are the modules: {orphan_module_names}")
    response = u.ask_user_confirmation("Do you want to uninstall?")
    return response
