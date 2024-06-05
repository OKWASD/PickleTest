import unittest
import pickle
import hashlib
import random

class MyClass:
    def __init__(self, data):
        self.data = data

class pickle_func_test(unittest.TestCase):
    def test_reversed_dict(self):
        obj = {"name": "Karl", "number": 420}
        obj2 = {"number": 420,"name": "Karl"}
        db = pickle.dumps(obj)
        db2 = pickle.dumps(obj2)
        load_db = pickle.loads(db)
        load_db2 = pickle.loads(db2)

        self.assertNotEqual(load_db, load_db2)

    def test_class(self):
        db = MyClass(42)
        test_db = pickle.dumps(db)
        unloaded = pickle.loads(test_db)

        self.assertEqual(db, unloaded)

    def test_value_of_class(self):
        db = MyClass(42)
        test_db = pickle.dumps(db)
        unloaded = pickle.loads(test_db)

        self.assertEqual(db.data, unloaded.data)

    def test_nested_dict(self):
        nested_dict = {'value': {"lock": "key"} , 'value2': {"name": "user"}, 'value3':{"animal": "dog"}}
        result = pickle.dumps(nested_dict)

        self.assertEqual(pickle.loads(result),nested_dict)

    def test_char_as_key(self):
        random_ascii_string =  ''.join(chr(random.randint(1,128)) for _ in range(1000))
        db = {random_ascii_string: "hej"}
        dump_db = pickle.dumps(db)
        load_db = pickle.loads(dump_db)
        
        self.assertEqual(db, load_db)

