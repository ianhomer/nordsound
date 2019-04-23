from .NordSound import NordSound
from .NordLead4Program import NordLead4Program
from .NordLead4Performance0 import NordLead4Performance0
from .NordLead4Performance1 import NordLead4Performance1

TYPES = {
    "nl4p.0": NordLead4Performance0,
    "nl4p.1": NordLead4Performance1,
    "nl4s.1": NordLead4Program
}
class NordSoundLoader:
    def load(self, filename):
        preload = NordSound(filename)
        soundClass = TYPES[preload.typeVersion]
        return soundClass(filename).verified()
