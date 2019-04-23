import os

from unittest import TestCase

from Data import Data
from nordsound.NordLead4Performance1 import NordLead4Performance1

class TestNordLead4Performance1(TestCase):
    def test_nord_lead_4_performance1(self):
        sound = NordLead4Performance1(Data().filename("init.nl4p")).verified()
        self.assertEqual(sound.type, "nl4p")
        self.assertEqual(sound.version, 1)
        self.assertEqual(sound.typeVersion, "nl4p.1")
        self.assertEqual(len(sound.programs), 4)
