from .SoundBlock import SoundBlock
from .NordLead4Performance import NordLead4Performance

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
""",'8B13x')

# Manual lists about 80 program properties
# + 6 morphs of a subset of these properties - say just below 40
PROGRAM_BLOCK = SoundBlock('Program',"""
    a
    b
    c
    d
    e
    f
    g
    h
""",'8B307x')

TAIL_BLOCK = SoundBlock('Tail',"""
    a
    b
""",'BB')

class NordLead4Performance0(NordLead4Performance):
    @property
    def performanceBlock(self):
        return PERFORMANCE_BLOCK

    @property
    def programBlock(self):
        return PROGRAM_BLOCK

    @property
    def tailBlock(self):
        return TAIL_BLOCK
