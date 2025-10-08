
from typing import Protocol

class Output(Protocol):

    def inc_ind(self) -> None: 
        """Increments the indent level"""
        ...

    def dec_ind(self) -> None: 
        """Increments the indent level"""
        ...

    @property
    def ind(self) -> str:
        """Returns the current indent"""
        ...

    def indent(self):
        """Context manager for an indented region"""
        ...
    
    def println(self, c : str) -> None:
        """Writes the specified content prefixed by the current 
        indent level and followed by a newline"""
        ...
    
    def write(self, c : str) -> None:
        """Writes the specified content to the output"""
        ...

    def close(self) -> None:
        """Performs any required cleanup work"""
        ...
