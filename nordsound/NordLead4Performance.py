import os, struct
from collections import namedtuple

from .logger import debug
from .NordSound import NordSound

class NordLead4Performance(NordSound):
    def __init__(self, filename):
        NordSound.__init__(self, filename)
        debug(filename)

    def __repr__(self):
        return str(self.performance) + ";" + ",".join(map(lambda x:str(x),self.programs)) + ";" + str(self.tail)

    def verified(self):        
        if self.size != self.expectedSize:
            raise Exception(f"Nord Lead 4 program file should be {self.expectedSize} bytes, it was {self.size}")
        return NordSound.verified(self)

    def parse(self, stream):
        NordSound.parse(self, stream)
        debug("NL4 parsing stream")
        self.performance = self.performanceBlock.parse(stream)
        self.programs = []
        for i in range(0,4):
            self.programs.append(
                self.programBlock.parse(stream)
            )
        self.tail = self.tailBlock.parse(stream)

    @property
    def expectedSize(self):
        return 12 + self.performanceBlock.length + 4 * self.programBlock.length + self.tailBlock.length

    @property
    def performanceBlock(self):
        raise NotImplementedError

    @property
    def programBlock(self):
        raise NotImplementedError

    @property
    def tailBlock(self):
        raise NotImplementedError
