from .NordSound import NordSound
from .NordLead4Program import NordLead4Program

TYPES = {
    "nl4p": NordLead4Program
}
class NordSoundLoader:
    def load(self, filename):
        preload = NordSound(filename)
        soundClass = TYPES[preload.type]
        return soundClass(filename)
