import os

class Data:
    def __init__(self):
        self.fileDirectory = os.path.dirname(__file__)
        self.dataDirectory = os.path.join(self.fileDirectory, 'data')

    def filename(self, relativeFilename):
        return os.path.join(self.dataDirectory, relativeFilename)
