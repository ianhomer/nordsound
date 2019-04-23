import os, io, struct

from collections import namedtuple
from .logger import debug

EXPECTED_HEAD = "CBIN"

class NordSound:
    def __init__(self, filename):
        filename = os.path.expanduser(str(filename))
        self.size = os.path.getsize(filename)
        with io.open(filename, 'rb') as stream:
            self.load(stream)

    def load(self, stream):
        self.parse(stream)

    def parse(self, stream):
        Head = namedtuple('Head','name type')
        head = Head._make(struct.unpack('4s4x4s', stream.read(12)))
        self.assertEquals(head.name, EXPECTED_HEAD, "Nord Sound file should start with")
        if self.toString(head.name) != EXPECTED_HEAD:
            raise Exception(f"Nord Sound file should start with {EXPECTED_HEAD}, it was {head}")
        self.type = self.toString(head.type)
        debug(f"Found {self.toString(head.type)}")

    def assertEquals(self, bytes, expected, message):
        s = self.toString(bytes)
        if s != expected:
            raise Exception(f"{message} {expected}, it was {s}")

    def toString(self, bytes):
        return bytes.decode('utf-8')
