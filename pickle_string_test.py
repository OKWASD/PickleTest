"""Contains tests for all things associated with strings"""
import unittest
import pickle
import random

class PickleStringTest(unittest.TestCase):
    """Class holding all string tests"""
    def test_ascii(self):
        """Tests if ASCII characters changes the way a string is dumped"""
        random_ascii_string =  ''.join(chr(random.randint(1,128)) for _ in range(1000))
        dump_string = pickle.dumps(random_ascii_string)
        load_string = pickle.loads(dump_string)

        self.assertEqual(random_ascii_string, load_string)

    def test_string_length(self):
        """Test if pickle can handle long strings"""
        random_string = ''.join(chr(random.randint(1,128)) for _ in range(1000000))
        dump_string = pickle.dumps(random_string)
        load_string = pickle.loads(dump_string)

        self.assertEqual(random_string, load_string)
