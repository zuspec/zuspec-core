import dataclasses as dc
import io
from typing import TextIO
from .output_stream import OutputStream

@dc.dataclass
class OutputString(OutputStream):
    fp : TextIO = dc.field(default_factory=lambda: io.StringIO())

    def getvalue(self) -> str:
        return self.fp.getvalue()


    
