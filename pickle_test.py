import pickle
import math
import unittest
import hashlib
import lorem
import random
from PIL import Image as PImage
import sys

class TestPickle(unittest.TestCase):

    def test_associative(self):
        db =  100 * math.pi
        db2 = math.pi * 100 # Floating-point calculation
        
        b = pickle.dumps(db)
        u = pickle.dumps(db2)

        load_b = pickle.loads(b)
        load_u = pickle.loads(u)
        
        self.assertEqual(load_u, load_b)

    def test_tuple(self):

        db = pickle.dumps((2, "Test"))
        db1 = pickle.dumps(("Test", 2))

        self.assertNotEqual(pickle.loads(db), pickle.loads(db1))

    def test_image(self):
        img = PImage.open("test.png")
        img_dump = pickle.dumps(img)
        img_load = pickle.loads(img_dump)

        self.assertEqual(img, img_load)

    def test_file_hash(self):   
        file = open('test.txt', "wb")
        data = lorem.text()
        pickle.dump(data,file)
        file.close()
        
        file = open('test.txt', "rb")
        load_file = pickle.load(file)
        hashed_load_file = hash(load_file)

        self.assertEqual(hash(data), hashed_load_file)
        file.close()
    
    def test_max_int(self):
        random_int =  int(''.join(str(random.randint(1,9)) for _ in range(4300)))
        
        random_int_dumps = pickle.dumps(random_int)
        random_int_loads = pickle.loads(random_int_dumps)

        self.assertEqual(random_int,random_int_loads)
