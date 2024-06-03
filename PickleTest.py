import pickle
import math
import unittest

class TestPickle(unittest.TestCase):
    def test_associative(self):
        db =  100* math.pi
        db2 = math.pi * 100 # Floating-point calculation
        
        b = pickle.dumps(db)
        u = pickle.dumps(db2)
        
        self.assertEqual(b, u)
    
    def test_nested_list(self):
        nested_list = [[[]],[[]],[[]]]
        nested_list.append(nested_list)
        
        g = pickle.dumps(nested_list)
        g_load = pickle.loads(g)
        
        self.assertEqual(nested_list, g_load)
        
def main():
    return        
        
if __name__ == '__main__':
    main()