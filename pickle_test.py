import pickle
import math
import unittest
import hashlib
from PIL import Image as PImage

class TestPickle(unittest.TestCase):

    def test_associative(self):
        db =  100* math.pi
        db2 = math.pi * 100 # Floating-point calculation
        
        b = pickle.dumps(db)
        u = pickle.dumps(db2)
        
        self.assertEqual(b, u)
    
    def test_reversed_dict(self):
        
        db = pickle.dumps({"name": "Johannes", "number": 420})
        db1 = pickle.dumps({"number": 420, "name": "Johannes"})

        self.assertNotEqual(db, db1)

    def test_tuple(self):

        db = pickle.dumps((2, "Test"))
        db1 = pickle.dumps(("Test", 2))

        self.assertNotEqual(pickle.loads(db), pickle.loads(db1))

    def test_image(self):
        img = PImage.open("test.png")
        img_dump = pickle.dumps(img)
        img_load = pickle.loads(img_dump)

        self.assertEqual(img, img_load)
