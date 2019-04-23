import os

from unittest import TestCase

from nordsound.tests.Data import Data
from nordsound.NordLead4Program import NordLead4Program, EXPECTED_SIZE

class TestNordLead4Program(TestCase):
    def test_nord_lead_4_program(self):
        sound = NordLead4Program(Data().filename("test.nl4p"))
        self.assertEqual(sound.size, EXPECTED_SIZE)
