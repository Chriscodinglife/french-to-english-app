"""
This script is a unit test for the translator.py script
"""

import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    """A set of tests for the methods written in the translator module"""

    def test1(self):
        """Tests for the French to English Method"""

        # Test for Null output for empty input
        self.assertRaises(TypeError, french_to_english)
        # Test for translating Hello to Bonjour
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test2(self):
        """Tests for the English to French Method"""

        # Test for Null output for empty input
        self.assertRaises(TypeError, english_to_french)
        # Test for translating Bonjour to Hello
        self.assertEqual(english_to_french("Hello"), "Bonjour")


unittest.main()