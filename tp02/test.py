#!/bin/python3
"""
Test all the functions of the package tp02
"""
from exo01 import exo01
from exo02 import exo02
from exo03 import exo03
from exo04 import exo04
from exo05 import exo05
from exo06 import exo06
from exo07 import exo07

from unittest import TestCase

class Test(TestCase):
    """
    Class containing the tests
    """
    def test_exo01(self):
        """
        Test of the function exo01
        """
        self.assertEqual(exo01("hel3lo"), [])
        self.assertEqual(exo01("hello"), ["hello"])
        self.assertEqual(exo01("Hello"), ["Hello"])
        self.assertEqual(exo01("Hello World"), [])
        self.assertEqual(exo01("HelloWorld"), ["HelloWorld"])
    
    def test_exo02(self):
        """
        Test of the function exo02
        """
        self.assertEqual(exo02("hello"), [])
        self.assertEqual(exo02("hel3lo"), ["3"])
        self.assertEqual(exo02("33"), ["33"])
        self.assertEqual(exo02("3.3"), ["3", "3"])
    
    def test_exo03(self):
        """
        Test of the function exo03
        """
        self.assertEqual(exo03("hello@hello.hello"), ["hello@hello.hello"])
        self.assertEqual(exo03("hello"), [])
        self.assertEqual(exo03("hello@wa"), [])
        self.assertEqual(exo03("3hello@wa.com"), [])
    
    def test_exo04(self):
        """
        Test of the function exo04
        """
        self.assertEqual(exo04("22-33-2020"), [])
        self.assertEqual(exo04("12-31-2020"), ["12-31-2020"])
        self.assertEqual(exo04("13-31-2020"), [])

    def test_exo05(self):
        """
        Test of the function exo04
        """
        self.assertEqual(exo05("pawwsa"), [])
        self.assertEqual(exo05("password05@"), ["password05@"])
        
