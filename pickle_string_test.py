import unittest
import pickle
import random

def random_int():     
    return random.randint(-1000, 1000)

def random_ascii():
    return chr(random_int() % 127)

class pickle_string_test(unittest.TestCase):

    def test(self):
        return


