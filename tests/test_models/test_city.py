#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8

class Testpep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        file_base_model = "models/base_model.py"
        check = style.check_files([file_base_model])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

class TestBase(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    """ def test_setid(self):
        self.assertEqual(self.b1.id, 7)

    def test_setid2(self):
        self.assertEqual(self.b2.id, 11)

    def test_setid3(self):
        self.assertEqual(self.b3.id, -1)

    def test_setid4(self):
        self.assertEqual(self.b4.id, 12)

    def test_setid5(self):
        self.assertEqual(self.b5.id, "hola")

    def test_setid6(self):
        self.assertEqual(self.b6.id, 3.1)

    def test_setid7(self):
        self.assertEqual(self.b7.id, 27)

    def test_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_json_string2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        list_back = json.loads(json_dictionary)
        self.assertEqual(list_back, [dictionary])
    """

if __name__ == '__main__':
    unittest.main()

