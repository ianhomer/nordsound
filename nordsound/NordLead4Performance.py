import os, struct
from collections import namedtuple

from .logger import debug
from .NordSound import NordSound

EXPECTED_SIZE = 1295

Performance = namedtuple('Performance','value')
PERFORMACE_FORMAT = 'b20x'
PERFORMACE_LENGTH = 21
Program = namedtuple('Program','value')
PROGRAM_FORMAT = 'b314x'
PROGRAM_LENGTH = 315
Tail = namedtuple('Tail','value')
TAIL_FORMAT = 'bx'
TAIL_LENGTH = 2

class NordLead4Performance(NordSound):
    def __init__(self, filename):
        NordSound.__init__(self, filename)
        if self.size != EXPECTED_SIZE:
            raise Exception(f"Nord Lead 4 program file should be {EXPECTED_SIZE} bytes, it was {self.size}")
        debug(filename)

    def __repr__(self):
        return str(self.performance) + ";" + ",".join(map(lambda x:str(x),self.programs)) + ";" + str(self.tail)

    def parse(self, stream):
        NordSound.parse(self, stream)
        debug("NL4 parsing stream")
        self.performance = Performance._make(struct.unpack(PERFORMACE_FORMAT, stream.read(PERFORMACE_LENGTH)))
        self.programs = []
        for i in range(0,4):
            self.programs.append(
                Performance._make(struct.unpack(PERFORMACE_FORMAT, stream.read(PERFORMACE_LENGTH)))
            )
        self.tail = Tail._make(struct.unpack(TAIL_FORMAT, stream.read(TAIL_LENGTH)))
