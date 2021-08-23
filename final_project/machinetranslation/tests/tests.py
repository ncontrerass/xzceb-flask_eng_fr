"""
This file contains a series of test.
"""
import unittest

from translator import englishtofrench, frenchtoenglish


class TestTranslator(unittest.TestCase):
    """
    This function tests translation from english to french
    """
    def test1(self):
        """
        Test - from english to french
        """
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertEqual(englishtofrench("How are you?"), "Comment es-tu?")
        self.assertRaises(ValueError,englishtofrench,None)


class TestEnglishToFrenchNull(unittest.TestCase):
    """
    This function tests for null input in english to french translation
    """
    def test2(self):
        """
        Test null
        """
        self.assertRaises(ValueError,englishtofrench,None)


class TestTranslatorFrench(unittest.TestCase):
    """
    This function tests translation from french to english
    """
    def test1(self):
        """
        Tests
        """
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")
        self.assertEqual(frenchtoenglish("Comment es-tu?"), "How are you?")
        self.assertRaises(ValueError,frenchtoenglish,None)


class TestFrenchToEnglishhNull(unittest.TestCase):
    """
    This function tests for null input in french to english translation
    """
    def test2(self):
        """
        Test null
        """
        self.assertRaises(ValueError,frenchtoenglish,None)

unittest.main()
