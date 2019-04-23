import os, struct
from collections import namedtuple

from .logger import debug
from .NordSound import NordSound

EXPECTED_SIZE = 1295

Performance = namedtuple('Performance','a b c d e f g h')
PERFORMACE_FORMAT = '8B13x'
PERFORMACE_LENGTH = 21
Program = namedtuple('Program','a b c d e f g h')
PROGRAM_FORMAT = '8B307x'
PROGRAM_LENGTH = 315
Tail = namedtuple('Tail','a b')
TAIL_FORMAT = 'BB'
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
                Program._make(struct.unpack(PROGRAM_FORMAT, stream.read(PROGRAM_LENGTH)))
            )
        self.tail = Tail._make(struct.unpack(TAIL_FORMAT, stream.read(TAIL_LENGTH)))
