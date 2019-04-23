import os, io

from .logger import debug
from .SoundBlock import SoundBlock

EXPECTED_HEAD = "CBIN"

NORD_HEAD_BLOCK = SoundBlock("NordHead","""
    name
    version
    type
    """,'4sB3x4s',12)

class NordSound:
    def __init__(self, filename):
        filename = os.path.expanduser(str(filename))
        self.size = os.path.getsize(filename)
        with io.open(filename, 'rb') as stream:
            self.load(stream)

    def load(self, stream):
        self.parse(stream)

    def parse(self, stream):
        self.head = self.headBlock.parse(stream)
        self.verified()
        self.type = self.toString(self.head.type)
        debug(f"Type = {self.type}")
        self.version = self.head.version
        self.typeVersion = self.type + "." + str(self.head.version)
        debug(f"Found {self.toString(self.head.type)}")

    def verified(self):
        self.assertEquals(self.head.name, EXPECTED_HEAD, "Nord Sound file should start with")
        if self.expectedSize > 0 and self.size != self.expectedSize:
            raise Exception(f"{type(self)} should be {self.expectedSize} bytes, it was {self.size}")
        return self

    def assertEquals(self, bytes, expected, message):
        s = self.toString(bytes)
        if s != expected:
            raise Exception(f"{message} {expected}, it was {s}")

    def toString(self, bytes):
        return bytes.decode('utf-8')

    @property
    def headBlock(self):
        return NORD_HEAD_BLOCK

    @property
    def expectedSize(self):
        return -1
