import pickle
import math
import unittest
import hashlib

class TestPickle(unittest.TestCase):
    def test_associative(self):
        db =  100* math.pi
        db2 = math.pi * 100 # Floating-point calculation
        
        b = pickle.dumps(db)
        u = pickle.dumps(db2)
        
        self.assertEqual(b, u)
    
    def test_nested_list(self):
        nested_list = [[[]],[[]],[[]]]
        
        g = pickle.dumps(nested_list)
        g_load = pickle.loads(g)
        
        self.assertEqual(nested_list, g_load)
        
    def test_hashing_equal(self):
        #Vi hashar 2st och self.assertEqual()
        
        db = pickle.dumps(first_to_second(1,2))
        db1 = pickle.dumps(second_to_first(1,2))
        
        hashed_db = hashlib.sha256(db)
        hashed_db1 = hashlib.sha256(db1)
                
        self.assertEqual(hashed_db.hexdigest(), hashed_db1.hexdigest())



def first_to_second(a,b):
    return a + b

def second_to_first(a,b):
    return b + a
        
if __name__ == '__main__':
    unittest.main()