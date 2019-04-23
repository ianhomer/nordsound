import os, struct

from .logger import debug
from .NordSound import NordSound

class NordLead4Performance(NordSound):
    def __init__(self, filename):
        NordSound.__init__(self, filename)
        debug(filename)

    def __repr__(self):
        return str(self.performance) + ";" + ",".join(map(lambda x:str(x),self.programs)) + ";" + str(self.tail)

    def parse(self, stream):
        NordSound.parse(self, stream)
        debug("NordLead4Performance : parsing stream")
        self.performance = self.performanceBlock.parse(stream)
        self.programs = []
        for i in range(0,4):
            self.programs.append(
                self.programBlock.parse(stream)
            )
        self.tail = self.tailBlock.parse(stream)

    @property
    def expectedSize(self):
        return self.headBlock.length + self.performanceBlock.length + 4 * self.programBlock.length + self.tailBlock.length

    @property
    def performanceBlock(self):
        raise NotImplementedError

    @property
    def programBlock(self):
        raise NotImplementedError

    @property
    def tailBlock(self):
        raise NotImplementedError
