import unittest
from dinosauron import cli
from dinosauron import dino_nmap

class TestDinoNmap(unittest.TestCase):
    def setUp(self):
        self.dn = dino_nmap.DinoNmap()

    def test_scan_list(self):
        l = self.dn.scan_list(["localhost"])
        self.assertIsInstance(l, list)
