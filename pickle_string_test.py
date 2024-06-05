import unittest
import pickle
import random

class pickle_string_test(unittest.TestCase):
    def test_ascii(self):
        random_ascii_string =  ''.join(chr(random.randint(1,128)) for _ in range(1000))
        dump_string = pickle.dumps(random_ascii_string)
        load_string = pickle.loads(dump_string)

        self.assertEqual(random_ascii_string, load_string)

    def test_string_length(self):
        random_string = ''.join(chr(random.randint(1,128)) for _ in range(1000000))
        dump_string = pickle.dumps(random_string)
        load_string = pickle.loads(dump_string)

        self.assertEqual(random_string, load_string)


thing = pickle_string_test()

thing.test_string_length()