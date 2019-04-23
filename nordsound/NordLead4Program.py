import os, struct

from .logger import debug
from .NordSound import NordSound
from .SoundBlock import SoundBlock

PROGRAM_HEAD_BLOCK = SoundBlock('ProgramHead',"""
    a
    b
    c
""",'3B31x',34)

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
""",'8B307x',315)

class NordLead4Program(NordSound):
    def __repr__(self):
        return str(self.programHead) + ";" + str(self.program)

    def parse(self, stream):
        NordSound.parse(self, stream)
        debug("NordLead4Program : parsing stream")
        self.programHead = self.programHeadBlock.parse(stream)
        self.program = self.programBlock.parse(stream)

    @property
    def programHeadBlock(self):
        return PROGRAM_HEAD_BLOCK

    @property
    def programBlock(self):
        return PROGRAM_BLOCK

    @property
    def expectedSize(self):
        return self.headBlock.length + self.programHeadBlock.length + self.programBlock.length
