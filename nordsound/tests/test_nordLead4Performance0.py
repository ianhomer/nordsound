import os

from unittest import TestCase

from Data import Data
from nordsound.NordLead4Performance0 import NordLead4Performance0

class TestNordLead4Performance0(TestCase):
    def test_nord_lead_4_performance0(self):
        sound = NordLead4Performance0(Data().filename("test.nl4p")).verified()
        self.assertEqual(sound.type, "nl4p")
        self.assertEqual(sound.version, 0)
        self.assertEqual(sound.typeVersion, "nl4p.0")
        self.assertEqual(len(sound.programs), 4)
        self.assertEqual(sound.performance.a, 1)
        self.assertEqual(sound.programs[1].a, 128)
        self.assertEqual(sound.tail.a, 195)
