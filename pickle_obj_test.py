"""Contains tests for all thing associated with objects"""
import unittest
import pickle
import random

class MyClass:
    """Mock class"""
    def __init__(self, data):
        self.data = data

    def get_data(self):
        """Returns data"""
        return self.data

    def get_data_reversed(self):
        """Returns the data reversed"""
        return self.data[::-1]

class MyClassEq:
    """Mock class with __eq__"""
    def __init__(self, data, data2):
        self.data = data
        self.data2 = data2

    def __eq__(self, other):
        """returns eq value"""
        if isinstance(other, MyClassEq):
            return self.data == other.data and self.data2 == other.data2
        return False

    def get_data(self):
        """Returns data"""
        return (self.data, self.data2)

class PickleFuncTest(unittest.TestCase):
    """Class containing all tests"""
    def test_reversed_dict(self):
        """Tests if pickling is dependent on order of list keys"""
        obj = {"name": "Karl", "number": 420}
        obj2 = {"number": 420,"name": "Karl"}
        data = pickle.dumps(obj)
        db2 = pickle.dumps(obj2)
        load_db = pickle.loads(data)
        load_db2 = pickle.loads(db2)

        self.assertNotEqual(load_db, load_db2)

    def test_class(self):
        """Tests if pickling changes the class instance"""
        data = MyClass(42)
        test_db = pickle.dumps(data)
        unloaded = pickle.loads(test_db)

        self.assertEqual(data, unloaded)

    def test_class_eq(self):
        """Tests if a class instance retains its equality after pickling and then loading"""
        data = MyClassEq(40, 42)
        pickled = pickle.dumps(data)

        load_pickle = pickle.loads(pickled)

        self.assertEqual(data, load_pickle)

    def test_value_of_class(self):
        """Tests if pickling changes the properties of a class instance"""
        data = MyClass(42)
        test_db = pickle.dumps(data)
        unloaded = pickle.loads(test_db)

        self.assertEqual(data.data, unloaded.data)

    def test_nested_dict(self):
        """Test pickling nested list"""
        nested_dict = {'value': {"lock": "key"} ,
                       'value2': {"name": "user"},
                       'value3':{"animal": "dog"}}
        result = pickle.dumps(nested_dict)

        self.assertEqual(pickle.loads(result),nested_dict)

    def test_char_as_key(self):
        """Test if random string can """
        random_ascii_string =  ''.join(chr(random.randint(1,128)) for _ in range(1000))
        data = {random_ascii_string: "hej"}
        dump_db = pickle.dumps(data)
        load_db = pickle.loads(dump_db)

        self.assertEqual(data, load_db)
