"""Testing the standard pickling cases"""
import pickle
import math
import unittest
import random
import lorem
from PIL import Image as PImage
import os

class TestPickle(unittest.TestCase):
    """Test cases for pickling"""
    def test_associative(self):
        """Test whether pickling is associative"""
        data =  100 * math.pi
        data2 = math.pi * 100 # Floating-point calculation
        dump_data = pickle.dumps(data)
        dump_data2 = pickle.dumps(data2)
        load_data = pickle.loads(dump_data)
        load_data2 = pickle.loads(dump_data2)

        self.assertEqual(load_data, load_data2)

    def test_tuple(self):
        """Test if touples can be pickled"""
        data = (2, "Test")
        data1 = pickle.dumps(data)
        load_data = pickle.loads(data1)

        self.assertEqual(data, load_data)

    def test_image(self):
        """Testing if images are the same before and after pickling"""
        img = PImage.open("test.png")
        img_dump = pickle.dumps(img)
        img_load = pickle.loads(img_dump)

        self.assertEqual(img, img_load)

    def test_file_hash(self):
        """Test hash of files"""
        with open('test.txt', "wb") as file:
            data = lorem.text()
            pickle.dump(data,file)

        with open('test.txt', "rb") as file:
            load_file = pickle.load(file)
            hashed_load_file = hash(load_file)

        self.assertEqual(hash(data), hashed_load_file)
        os.remove("./test.txt")

    def test_max_int(self):
        """Testing if pickling can handle max int length"""
        random_int = int(''.join(str(random.randint(1,9)) for _ in range(4300)))
        random_int_dumps = pickle.dumps(random_int)
        random_int_loads = pickle.loads(random_int_dumps)
        self.assertEqual(random_int,random_int_loads)

    def test_double_dump(self):
        """Testing if pickling twice will change data"""
        dump = "Test"
        dump1 = pickle.dumps(dump)
        dump2 = pickle.dumps(dump1)

        load_dump2 = pickle.loads(dump2)
        load_dump1 = pickle.loads(load_dump2)

        self.assertEqual(dump, load_dump1)
