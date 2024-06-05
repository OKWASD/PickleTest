"""Testing lists"""
import unittest
import pickle

def same_hash(a_variable,b_variable):
    """Returns true of both are same"""
    return hash(a_variable) == hash(b_variable)

class PickleListTest(unittest.TestCase):
    """Class containing all tests associated with lists"""
    def test_deep_list(self):
        """"6. Test if pickle can handle deep lists"""
        data = [[]]
        nested = data[0]
        for _ in range(300):
            nested.append([])
            nested = nested[0]

        pickled_data = pickle.dumps(data)
        loaded_data = pickle.loads(pickled_data)

        self.assertEqual(data, loaded_data)

    def test_double_list(self):
        """7. Tests how pickling handles nested lists."""
        self.assertEqual(pickle.dumps([[],[]]), pickle.dumps([[],[]]))

    def test_double_false_list(self):
        """8. Tests if two lists with different orders are considered equal when pickled."""
        self.assertNotEqual(pickle.dumps([[1],[2]]), pickle.dumps([[2],[1]]))
