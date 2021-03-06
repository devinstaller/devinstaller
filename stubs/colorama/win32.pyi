from ctypes import Structure
from typing import Any

STDOUT: int
STDERR: int
windll: Any
SetConsoleTextAttribute: Any
winapi_test: Any
COORD: Any

class CONSOLE_SCREEN_BUFFER_INFO(Structure): ...

def GetConsoleScreenBufferInfo(stream_id: Any = ...): ...
def SetConsoleCursorPosition(stream_id: Any, position: Any, adjust: bool = ...): ...
def FillConsoleOutputCharacter(stream_id: Any, char: Any, length: Any, start: Any): ...
def FillConsoleOutputAttribute(stream_id: Any, attr: Any, length: Any, start: Any): ...
def SetConsoleTitle(title: Any): ...
