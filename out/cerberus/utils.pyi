from cerberus.platform import Mapping as Mapping, Sequence as Sequence, Set as Set
from collections import namedtuple
from typing import Any, Optional

TypeDefinition = namedtuple('TypeDefinition', 'name,included_types,excluded_types')

def compare_paths_lt(x: Any, y: Any): ...
def drop_item_from_tuple(t: Any, i: Any): ...
def get_Validator_class(): ...
def mapping_hash(schema: Any): ...
def mapping_to_frozenset(mapping: Any): ...
def quote_string(value: Any): ...

class readonly_classproperty(property):
    def __get__(self, instance: Any, owner: Any): ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

def validator_factory(name: Any, bases: Optional[Any] = ..., namespace: Any = ...): ...
