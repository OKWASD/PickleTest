"""Testing the result of pickling functions."""

import unittest
import pickle

class PickleFuncTest(unittest.TestCase):
    """Testing pickling functions"""
    def test_hashing_equal(self):
        """Test whether a function containing add function is pickled correctly"""
        data = pickle.dumps(add_operator)
        load_data = pickle.loads(data)
        self.assertEqual(hash(add_operator), hash(load_data))

    def test_or_operator(self):
        """Test whether a function containing the or logic operator is pickled correctly"""
        data = pickle.dumps(or_operator)
        load_data = pickle.loads(data)
        self.assertEqual(hash(or_operator), hash(load_data))

    def test_xor_operator(self):
        """Tests XOR operator before and after loading"""
        data = pickle.dumps(xor_operator)
        load_data = pickle.loads(data)
        self.assertEqual(hash(xor_operator), hash(load_data))

    def test_and_operator(self):
        """Testing and operator"""
        data = pickle.dumps(and_operator)
        load_data = pickle.loads(data)
        self.assertEqual(hash(and_operator), hash(load_data))

    def test_lambda_func(self):
        """Testing lambda functions"""
        og_lamb = lambda x: x * 2

        try:
            lamb = pickle.dumps(og_lamb)
            _ = pickle.loads(lamb)
        except AttributeError:
            self.assertRaises(AttributeError)

def add_operator(a_variable,b_variable):
    """Returns sum"""
    return a_variable + b_variable

def or_operator(a_variable,b_variable):
    """Returns or"""
    return a_variable | b_variable

def and_operator(a_variable,b_variable):
    """Returns and"""
    return a_variable & b_variable

def xor_operator(a_variable,b_variable):
    """Returns xor"""
    return a_variable ^ b_variable
