import unittest
from dinosauron import dino_nmap
from unittest.mock import create_autospec

class TestDinoNmap(unittest.TestCase):
    def setUp(self):
        self.dn = dino_nmap.DinoNmap()

    def test_scan_list(self):
        args = '192.168.0.*'
        mock = create_autospec(self.dn.scan_list, return_value=[])
        mock(args)
        mock.assert_called_once_with(args)

    def test_do_scan(self):
        args = [["192.168.1.1"], "-sV"]
        mock_function = create_autospec(self.dn.do_scan, return_value=[])
        mock_function(*args)
        mock_function.assert_called_once_with(*args)
