from cerberus.platform import MutableMapping as MutableMapping, PYTHON_VERSION as PYTHON_VERSION
from cerberus.utils import compare_paths_lt as compare_paths_lt, quote_string as quote_string
from collections import namedtuple
from typing import Any, Optional

ErrorDefinition = namedtuple('ErrorDefinition', 'code, rule')
CUSTOM: Any
DOCUMENT_MISSING: Any
REQUIRED_FIELD: Any
UNKNOWN_FIELD: Any
DEPENDENCIES_FIELD: Any
DEPENDENCIES_FIELD_VALUE: Any
EXCLUDES_FIELD: Any
DOCUMENT_FORMAT: Any
EMPTY_NOT_ALLOWED: Any
NOT_NULLABLE: Any
BAD_TYPE: Any
BAD_TYPE_FOR_SCHEMA: Any
ITEMS_LENGTH: Any
MIN_LENGTH: Any
MAX_LENGTH: Any
REGEX_MISMATCH: Any
MIN_VALUE: Any
MAX_VALUE: Any
UNALLOWED_VALUE: Any
UNALLOWED_VALUES: Any
FORBIDDEN_VALUE: Any
FORBIDDEN_VALUES: Any
MISSING_MEMBERS: Any
NORMALIZATION: Any
COERCION_FAILED: Any
RENAMING_FAILED: Any
READONLY_FIELD: Any
SETTING_DEFAULT_FAILED: Any
ERROR_GROUP: Any
MAPPING_SCHEMA: Any
SEQUENCE_SCHEMA: Any
KEYSRULES: Any
KEYSCHEMA: Any
VALUESRULES: Any
VALUESCHEMA: Any
BAD_ITEMS: Any
LOGICAL: Any
NONEOF: Any
ONEOF: Any
ANYOF: Any
ALLOF: Any
SCHEMA_ERROR_DEFINITION_TYPE: str
SCHEMA_ERROR_MISSING: str

class ValidationError:
    document_path: Any = ...
    schema_path: Any = ...
    code: Any = ...
    rule: Any = ...
    constraint: Any = ...
    value: Any = ...
    info: Any = ...
    def __init__(self, document_path: Any, schema_path: Any, code: Any, rule: Any, constraint: Any, value: Any, info: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    @property
    def child_errors(self): ...
    @property
    def definitions_errors(self): ...
    @property
    def field(self): ...
    @property
    def is_group_error(self): ...
    @property
    def is_logic_error(self): ...
    @property
    def is_normalization_error(self): ...

class ErrorList(list):
    def __contains__(self, error_definition: Any): ...

class ErrorTreeNode(MutableMapping):
    parent_node: Any = ...
    tree_root: Any = ...
    path: Any = ...
    errors: Any = ...
    descendants: Any = ...
    def __init__(self, path: Any, parent_node: Any) -> None: ...
    def __contains__(self, item: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, item: Any): ...
    def __len__(self): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    @property
    def depth(self): ...
    @property
    def tree_type(self): ...
    def add(self, error: Any) -> None: ...

class ErrorTree(ErrorTreeNode):
    parent_node: Any = ...
    tree_root: Any = ...
    path: Any = ...
    errors: Any = ...
    descendants: Any = ...
    def __init__(self, errors: Any = ...) -> None: ...
    def add(self, error: Any) -> None: ...
    def fetch_errors_from(self, path: Any): ...
    def fetch_node_from(self, path: Any): ...

class DocumentErrorTree(ErrorTree):
    tree_type: str = ...

class SchemaErrorTree(ErrorTree):
    tree_type: str = ...

class BaseErrorHandler:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, errors: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def add(self, error: Any) -> None: ...
    def emit(self, error: Any) -> None: ...
    def end(self, validator: Any) -> None: ...
    def extend(self, errors: Any) -> None: ...
    def start(self, validator: Any) -> None: ...

class ToyErrorHandler(BaseErrorHandler):
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    def clear(self) -> None: ...

def encode_unicode(f: Any): ...

class BasicErrorHandler(BaseErrorHandler):
    messages: Any = ...
    tree: Any = ...
    def __init__(self, tree: Optional[Any] = ...) -> None: ...
    def __call__(self, errors: Any): ...
    @property
    def pretty_tree(self): ...
    def add(self, error: Any) -> None: ...
    def clear(self) -> None: ...
    def start(self, validator: Any) -> None: ...

class SchemaErrorHandler(BasicErrorHandler):
    messages: Any = ...
