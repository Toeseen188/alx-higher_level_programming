#!/usr/bin/python3
"""this module contains unittest"""
from models import base
from models.base import Base
import unittest


class TestDocumentation(unittest.TestCase):
    """ Testing if Documentation is available"""

    def test_base_module_doc(self):
        """ base module doc"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_base_class_doc(self):
        """ base class doc"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_base_init_doc(self):
        """init doc"""
        self.assertTrue(len(Base.__init__.__doc__) > 0)



class TestBaseClass(unittest.TestCase):
    """ this class test for correctness
    and error in Base class"""

    def test_base_id(self):
        """ testing for Base parameter"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)
        
        b4 = Base()
        self.assertEqual(b4.id, 4)

        b54 = Base(54)
        self.assertEqual(b54.id, 54)

        b_neg = Base(-81)
        self.assertEqual(b_neg.id, -81)

        b_none = Base(None)
        self.assertEqual(b_none.id, 5)

if __name__ == "__main__":
    unittest.main()
