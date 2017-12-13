import unittest
from dinosauron import dinosauron 
from unittest.mock import create_autospec

class TestDinosauron(unittest.TestCase):
    def setUp(self):
        self.d = dinosauron.Dinosauron()

    def test_dig_mdns(self):
        mock = create_autospec(self.d.dig_mdns, return_value='')
        args = '127.0.0.1'
        mock(args)
        mock.assert_called_once_with(args)
