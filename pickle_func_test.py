import unittest
import pickle
import hashlib

class pickle_func_test(unittest.TestCase):
    def test_hashing_equal(self):
        db = pickle.dumps(first_to_second)
        load_db = pickle.loads(db)
        self.assertEqual(hash(first_to_second), hash(load_db))

    def test_lambda_func(self):
        try:
            pickle.dumps(lambda x: x+1)
        except Exception:
            self.assertRaises(TypeError)

def first_to_second(a,b):
    return a + b
