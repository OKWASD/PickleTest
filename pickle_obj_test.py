import unittest
import pickle
import hashlib

class MyClass:
    def __init__(self, data):
        self.data = data

class pickle_func_test(unittest.TestCase):
    def test_reversed_dict(self):
        
        db = pickle.dumps({"name": "Johannes", "number": 420})
        db1 = pickle.dumps({"number": 420, "name": "Johannes"})

        self.assertNotEqual(db, db1)

    def test_class(self):

        db = MyClass(42)

        test_db = pickle.dumps(db)
        
        unloaded = pickle.loads(test_db)
        
        self.assertNotEqual(db, unloaded)
    
    def test_value_of_class(self):

        db = MyClass(42)

        test_db = pickle.dumps(db)
        
        unloaded = pickle.loads(test_db)

        self.assertEqual(db.data, unloaded.data)

    def test_nested_dict(self):
        nested_dict = {'value': {"lock": "key"} , 'hello': {"name": "user"}, 'boy':{"animal": "dog"}}
        result = pickle.dumps(nested_dict)

        self.assertEqual(pickle.loads(result),nested_dict)

