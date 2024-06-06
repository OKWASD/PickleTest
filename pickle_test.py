"""Testing the standard pickling cases"""
import pickle
import math
import unittest
import random
import os
import lorem
from PIL import Image as PImage


class TestPickle(unittest.TestCase):
     # pylint: disable=too-many-public-methods
    """Test cases for pickling"""
    def test_associative(self):
        """17. Test whether pickling is associative"""
        data =  100 * math.pi
        data2 = math.pi * 100 # Floating-point calculation
        dump_data = pickle.dumps(data)
        dump_data2 = pickle.dumps(data2)
        load_data = pickle.loads(dump_data)
        load_data2 = pickle.loads(dump_data2)

        self.assertEqual(load_data, load_data2)

    def test_tuple(self):
        """18. Test if tuples can be pickled"""
        data = (2, "Test")
        data1 = pickle.dumps(data)
        load_data = pickle.loads(data1)

        self.assertEqual(data, load_data)

    def test_image(self):
        """19. Testing if images are the same before and after pickling"""
        img = PImage.open("test.png")
        img_dump = pickle.dumps(img)
        img_load = pickle.loads(img_dump)

        self.assertEqual(img, img_load)

    def test_file_hash(self):
        """20. Test hash of files"""
        with open('test.txt', "wb") as file:
            data = lorem.text()
            pickle.dump(data,file)

        with open('test.txt', "rb") as file:
            load_file = pickle.load(file)
            hashed_load_file = hash(load_file)

        self.assertEqual(hash(data), hashed_load_file)
        os.remove("./test.txt")

    def test_max_int(self):
        """21. Testing if pickling can handle max int length"""
        random_int = int(''.join(str(random.randint(1,9)) for _ in range(4300)))
        random_int_dumps = pickle.dumps(random_int)
        random_int_loads = pickle.loads(random_int_dumps)
        self.assertEqual(random_int,random_int_loads)

    def test_double_dump(self):
        """22. Testing if pickling twice will change data"""
        dump = "Test"
        dump1 = pickle.dumps(dump)
        dump2 = pickle.dumps(dump1)

        load_dump2 = pickle.loads(dump2)
        load_dump1 = pickle.loads(load_dump2)

        self.assertEqual(dump, load_dump1)

    def test_pickle_true(self):
        """"23. Testing if pickling can handle the value True"""
        dump = pickle.dumps(True)
        self.assertEqual(True, pickle.loads(dump))

    def test_pickle_none(self):
        """"24. Testing if pickling can handle the value None"""
        dump = pickle.dumps(None)
        self.assertEqual(None, pickle.loads(dump))

    def test_pickle_false(self):
        """"25. Testing if pickling can handle the value False"""
        dump = pickle.dumps(False)
        self.assertEqual(False, pickle.loads(dump))

    def test_pickle_inf(self):
        """"26. Testing if pickling can handle Infinity"""
        dump = pickle.dumps(float('inf'))
        self.assertEqual(float('inf'), pickle.loads(dump))

    def test_pickle_negative_inf(self):
        """"27. Testing if pickling can handle negative Infinity"""
        dump = pickle.dumps(float('-inf'))
        self.assertEqual(float('-inf'), pickle.loads(dump))

    def test_complex_numbers(self):
        """"28. Testing if pickling can handle complex numbers"""
        number = complex(1,2)
        dump = pickle.dumps(number)
        self.assertEqual(number, pickle.loads(dump))

    def test_structure_set(self):
        """29. Testing if pickling changes a set"""
        test_set = {"apple", "banana", "cherry"}
        dump = pickle.dumps(test_set)
        self.assertEqual(test_set, pickle.loads(dump))

    def test_bytes(self):
        """30. Testing if pickling changes bytes"""
        data = b'101'
        dump = pickle.dumps(data)
        self.assertEqual(data, pickle.loads(dump))

    def test_bytearray(self):
        """31. Testing if pickling changes a bytearray"""
        numbers = [1, 3, 5, 7, 11]
        numbers_bytearray = bytearray(numbers)
        dump = pickle.dumps(numbers_bytearray)
        self.assertEqual(numbers_bytearray, pickle.loads(dump))

    def test_ellipsis(self):
        """32. Testing if pickling can handle ellipsis"""
        dump = pickle.dumps(...)
        self.assertEqual(..., pickle.loads(dump))

    def test_ellipsis_in_list(self):
        """33. Testing if pickling can handle ellipsis in a list"""
        data = [...]
        dump = pickle.dumps(data)
        self.assertEqual(data, pickle.loads(dump))

    def test_ellipsis_in_dict(self):
        """34. Testing if pickling can handle ellipsis in a dictionary"""
        data = {"key": ...}
        dump = pickle.dumps(data)
        self.assertEqual(data, pickle.loads(dump))

    def test_ellipsis_in_set(self):
        """35. Testing if pickling can handle ellipsis in a set"""
        data = {...}
        dump = pickle.dumps(data)
        self.assertEqual(data, pickle.loads(dump))

    def test_ellipsis_in_touple(self):
        """36. Testing if pickling can handle ellipsis in a tuple"""
        data = ("key", ...)
        dump = pickle.dumps(data)
        self.assertEqual(data, pickle.loads(dump))

    def test_set_in_dict(self):
        """37. Testing if pickling can handle sets in dictionaries"""
        data = {"key": {1,2,3,4}}
        dump = pickle.dumps(data)
        self.assertEqual(data, pickle.loads(dump))

    def test_deep_dict(self):
        """38. Testing if pickling can handle deep dictionaries"""
        data = {"start": {}}
        index = data["start"]
        for _ in range(300):
            index[str(_)] = {}
            index = index[str(_)]

        pickled_data = pickle.dumps(data)
        unpickled_data = pickle.loads(pickled_data)

        self.assertEqual(data, unpickled_data)
