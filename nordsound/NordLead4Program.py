import os
from .logger import debug

EXPECTED_SIZE = 1295

class NordLead4Program:
    def __init__(self, filename):
        filename = os.path.expanduser(str(filename))
        self.size = os.path.getsize(filename)
        if self.size != EXPECTED_SIZE:
            raise Exception(f"Nord Lead 4 program file should be {EXPECTED_SIZE} bytes")
        debug(filename)
