import unittest
import pickle

def sameHash(a,b):
    return hash(a) == hash(b)

class pickle_list_test(unittest.TestCase):
    def test_deep_list(self):
        data = [[]]
        nested = data[0]
        for i in range(300):
            nested.append([])
            nested = nested[0]
        
        pickled_data = pickle.dumps(data)
        loaded_data = pickle.loads(pickled_data)

        self.assertEqual(data, loaded_data)

    def test_double_list(self):
        self.assertEqual(pickle.dumps([[],[]]), pickle.dumps([[],[]]))

    def test_double_false_list(self):
        self.assertNotEqual(pickle.dumps([[1],[2]]), pickle.dumps([[2],[1]]))

