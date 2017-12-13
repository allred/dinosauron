import unittest
from dinosauron import dino_nmap
from unittest.mock import create_autospec

class TestDinoNmap(unittest.TestCase):
    def setUp(self):
        self.dn = dino_nmap.DinoNmap()

    def test_scan_list(self):
        l = self.dn.scan_list(["localhost"])
        self.assertIsInstance(l, list)
        self.assertEqual(len(l), 1)

    def test_do_scan(self):
        mock_function = create_autospec(self.dn.do_scan, return_value=[])
        args = [["192.168.1.1"], "-sV"]
        mock_function(*args)
        mock_function.assert_called_once_with(*args)
