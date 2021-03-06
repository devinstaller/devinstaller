from .ansi import AnsiBack as AnsiBack, AnsiFore as AnsiFore, AnsiStyle as AnsiStyle, Style as Style
from .win32 import winapi_test as winapi_test, windll as windll
from .winterm import WinColor as WinColor, WinStyle as WinStyle, WinTerm as WinTerm
from typing import Any, Optional

winterm: Any

class StreamWrapper:
    def __init__(self, wrapped: Any, converter: Any) -> None: ...
    def __getattr__(self, name: Any): ...
    def __enter__(self, *args: Any, **kwargs: Any): ...
    def __exit__(self, *args: Any, **kwargs: Any): ...
    def write(self, text: Any) -> None: ...
    def isatty(self): ...
    @property
    def closed(self): ...

class AnsiToWin32:
    ANSI_CSI_RE: Any = ...
    ANSI_OSC_RE: Any = ...
    wrapped: Any = ...
    autoreset: Any = ...
    stream: Any = ...
    strip: Any = ...
    convert: Any = ...
    win32_calls: Any = ...
    on_stderr: Any = ...
    def __init__(self, wrapped: Any, convert: Optional[Any] = ..., strip: Optional[Any] = ..., autoreset: bool = ...) -> None: ...
    def should_wrap(self): ...
    def get_win32_calls(self): ...
    def write(self, text: Any) -> None: ...
    def reset_all(self) -> None: ...
    def write_and_convert(self, text: Any) -> None: ...
    def write_plain_text(self, text: Any, start: Any, end: Any) -> None: ...
    def convert_ansi(self, paramstring: Any, command: Any) -> None: ...
    def extract_params(self, command: Any, paramstring: Any): ...
    def call_win32(self, command: Any, params: Any) -> None: ...
    def convert_osc(self, text: Any): ...
