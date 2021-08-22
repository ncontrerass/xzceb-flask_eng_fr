"""
This file contains a series of test.
"""
import unittest

from translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    """
    This function tests translation from english to french
    """
    def test1(self):
        """
        Test - from english to french
        """
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("How are you?"), "Comment es-tu?")
        self.assertRaises(ValueError,englishToFrench,None)


class TestEnglishToFrenchNull(unittest.TestCase):
    """
    This function tests for null input in english to french translation
    """
    def test2(self):
        """
        Test null
        """
        self.assertRaises(ValueError,englishToFrench,None)


class TestTranslatorFrench(unittest.TestCase):
    """
    This function tests translation from french to english
    """
    def test1(self):
        """
        Tests
        """
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish("Comment es-tu?"), "How are you?")
        self.assertRaises(ValueError,frenchToEnglish,None)


class TestFrenchToEnglishhNull(unittest.TestCase):
    """
    This function tests for null input in french to english translation
    """
    def test2(self):
        """
        Test null
        """
        self.assertRaises(ValueError,frenchToEnglish,None)

unittest.main()
