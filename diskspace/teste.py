import os
import re
import unittest
from diskspace import bytes_to_readable, subprocess_check_output, show_space_list

class TestBytes_to_readable(unittest.TestCase):

    def test_show_space_list(self):
        self.assertIsNone(show_space_list(directory='.', depth=-1, order=True))

    def test_bytes_to_readable(self):
        bytes = bytes_to_readable(2)
        self.assertEqual(bytes, '1.00Kb')
        self.assertIsNotNone(bytes)

    def subprocess_check_output(self):
        command = 'du '
        subprocess = subprocess_check_output(command)
        self.assertIsInstance(command, str)

if __name__ == '__main__':
    unittest.main()
