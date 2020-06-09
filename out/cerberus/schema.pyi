from cerberus import errors as errors
from cerberus.platform import Callable as Callable, Hashable as Hashable, Mapping as Mapping, MutableMapping as MutableMapping, Sequence as Sequence
from cerberus.utils import TypeDefinition as TypeDefinition, get_Validator_class as get_Validator_class, mapping_hash as mapping_hash, validator_factory as validator_factory
from typing import Any, Optional

class _Abort(Exception): ...
class SchemaError(Exception): ...

class DefinitionSchema(MutableMapping):
    def __new__(cls, *args: Any, **kwargs: Any): ...
    validator: Any = ...
    validation_schema: Any = ...
    schema_validator: Any = ...
    schema: Any = ...
    def __init__(self, validator: Any, schema: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __getitem__(self, item: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def copy(self): ...
    @classmethod
    def expand(cls, schema: Any): ...
    def get(self, item: Any, default: Optional[Any] = ...): ...
    def items(self): ...
    def update(self, schema: Any) -> None: ...
    def regenerate_validation_schema(self) -> None: ...
    def validate(self, schema: Optional[Any] = ...) -> None: ...

class UnvalidatedSchema(DefinitionSchema):
    schema: Any = ...
    def __init__(self, schema: Any = ...) -> None: ...
    def validate(self, schema: Any) -> None: ...
    def copy(self): ...

class SchemaValidationSchema(UnvalidatedSchema):
    schema: Any = ...
    def __init__(self, validator: Any) -> None: ...

class SchemaValidatorMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def known_rules_set_refs(self): ...
    @property
    def known_schema_refs(self): ...
    @property
    def target_schema(self): ...
    @property
    def target_validator(self): ...

class Registry:
    def __init__(self, definitions: Any = ...) -> None: ...
    def add(self, name: Any, definition: Any) -> None: ...
    def all(self): ...
    def clear(self) -> None: ...
    def extend(self, definitions: Any) -> None: ...
    def get(self, name: Any, default: Optional[Any] = ...): ...
    def remove(self, *names: Any) -> None: ...

class SchemaRegistry(Registry): ...
class RulesSetRegistry(Registry): ...

schema_registry: Any
rules_set_registry: Any