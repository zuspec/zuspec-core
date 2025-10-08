import dataclasses as dc
from typing import TextIO
from .output import Output

@dc.dataclass
class OutputStream(Output):
    fp : TextIO = dc.field()
    _ind : str = dc.field(default="")

    def inc_ind(self) -> None: 
        """Increments the indent level"""
        self._ind += "    "

    def dec_ind(self) -> None: 
        """Increments the indent level"""
        if len(self._ind) > 4:
            self._ind = self._ind[4:]
        else:
            self._ind = ""

    @property
    def ind(self) -> str:
        """Returns the current indent"""
        return self._ind

    def indent(self):
        """Context manager for an indented region"""
        class Ctxt(object):
            def __init__(self, out):
                self.out = out
            def __enter__(self):
                self.out.inc_ind()
            def __exit__(self, e, t, tb):
                self.out.dec_ind()
        return Ctxt(self)
    
    def println(self, c : str) -> None:
        """Writes the specified content prefixed by the current 
        indent level and followed by a newline"""
        self.fp.write(self._ind)
        self.fp.write(c)
        self.fp.write("\n")
    
    def write(self, c : str) -> None:
        """Writes the specified content to the output"""
        self.fp.write(c)

    def close(self) -> None:
        """Performs any required cleanup work"""
        self.fp.close()

    
