import unittest
import pickle
import hashlib

class pickle_func_test(unittest.TestCase):
    def test_hashing_equal(self):
        
        db = pickle.dumps(first_to_second)
        db1 = pickle.dumps(second_to_first)

        hashed_db = hashlib.sha256(db)
        hashed_db1 = hashlib.sha256(db1)
                
        self.assertNotEqual(hashed_db.hexdigest(), hashed_db1.hexdigest())

    def test_lambda_func(self):
        try:
            pickle.dumps(lambda x: x+1)
        except Exception:
            self.assertRaises(TypeError)


def first_to_second(a,b):
    return a + b

def second_to_first(a,b):
    return b + a
