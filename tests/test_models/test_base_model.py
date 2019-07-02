#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.base_model import BaseModel
import os


class Testpep8(unittest.TestCase):
    """ test pep8 """
    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_base_model = "models/base_model.py"
        file_test_base_model = "tests/test_models/test_base_model.py"
        check = style.check_files([file_base_model, file_test_base_model])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBase(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ first set up """
        cls.ins = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ final statement """
        del cls.ins
        try:
            os.remove("file.json")
        except:
            pass

    def setUp(self):
        """ first set up before test """
        pass

    def tearDown(self):
        """ final statement after test """
        pass

    def test_BaseModeldoc(self):
        """ test base model documentation
        self.assertNotEqual(len(models.__doc__), 0)
        self.assertNotEqual(len(models.base_model.__doc__), 0)

        """
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "id"), True)
        self.assertEqual(hasattr(self.ins, "created_at"), True)
        self.assertEqual(hasattr(self.ins, "updated_at"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.ins, BaseModel))

    def test_save_updated_at_created_at(self):
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)

    def test_dict(self):
        dicto = self.ins.to_dict()
        self.assertTrue(dicto.get("__class__"))
        self.assertTrue(type(dicto) is dict)
        self.assertTrue("to_dict" in dir(self.ins))

if __name__ == '__main__':
    unittest.main()
