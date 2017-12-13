import unittest
from dinosauron import dinosauron 
from unittest.mock import create_autospec

class TestDinoNmap(unittest.TestCase):
    def setUp(self):
        self.dn = dino_nmap.DinoNmap()
