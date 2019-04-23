import struct
from collections import namedtuple

class SoundBlock:
    def __init__(self, name, fieldNames, format, length):
        self.tuple = namedtuple(name, fieldNames)
        self.format = format
        self.length = length

    def parse(self, stream):
        if self.length == 0:
            return ()
        return self.tuple._make(struct.unpack(self.format, stream.read(self.length)))
