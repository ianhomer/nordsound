import os

from unittest import TestCase

from nordsound.tests.Data import Data
from nordsound.NordLead4Performance import NordLead4Performance, EXPECTED_SIZE

class TestNordLead4Performance(TestCase):
    def test_nord_lead_4_performance(self):
        sound = NordLead4Performance(Data().filename("test.nl4p"))
        self.assertEqual(sound.size, EXPECTED_SIZE)
        self.assertEqual(sound.type, "nl4p")
        self.assertEqual(len(sound.programs), 4)
