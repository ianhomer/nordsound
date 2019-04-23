import os

from unittest import TestCase

from Data import Data
from nordsound.NordLead4Program import NordLead4Program

class TestNordLead4Program(TestCase):
    def test_nord_lead_4_program(self):
        sound = NordLead4Program(Data().filename("init.nl4s")).verified()
        self.assertEqual(sound.type, "nl4s")
        self.assertEqual(sound.version, 1)
        self.assertEqual(sound.typeVersion, "nl4s.1")
