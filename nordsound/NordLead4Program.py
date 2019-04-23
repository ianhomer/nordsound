import os
from struct import unpack

from .logger import debug
from .NordSound import NordSound

EXPECTED_SIZE = 1295

class NordLead4Program(NordSound):
    def __init__(self, filename):
        NordSound.__init__(self, filename)
        if self.size != EXPECTED_SIZE:
            raise Exception(f"Nord Lead 4 program file should be {EXPECTED_SIZE} bytes, it was {self.size}")
        debug(filename)

    def parse(self, stream):
        NordSound.parse(self, stream)
        debug("NL4 parsing stream")
