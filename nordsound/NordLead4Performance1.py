from .SoundBlock import SoundBlock
from .NordLead4Performance import NordLead4Performance
from .NordLead4Program import PROGRAM_BLOCK

# Manual list 10 performance level properties + 12(?) characters for name
PERFORMANCE_BLOCK = SoundBlock('Performance',"""
    a
    b
    c
    d
    e
    f
    g
    h
""",'8B33x')

TAIL_BLOCK = SoundBlock('Tail','','')

class NordLead4Performance1(NordLead4Performance):
    @property
    def performanceBlock(self):
        return PERFORMANCE_BLOCK

    @property
    def programBlock(self):
        return PROGRAM_BLOCK

    @property
    def tailBlock(self):
        return TAIL_BLOCK
