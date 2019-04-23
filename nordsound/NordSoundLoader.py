from .NordSound import NordSound
from .NordLead4Performance import NordLead4Performance

TYPES = {
    "nl4p": NordLead4Performance
}
class NordSoundLoader:
    def load(self, filename):
        preload = NordSound(filename)
        soundClass = TYPES[preload.type]
        return soundClass(filename)
