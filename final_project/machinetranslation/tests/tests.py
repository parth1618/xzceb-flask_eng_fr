""" Unit Test File for Translation Functions """

import unittest
import translator #pylint: disable=E401


class TestLanguageTranslation(unittest.TestCase):
    """ Unit Test class to test language translation """

    def test_english_to_french_valid_input(self):
        """Test English to French Translation - Valid Input"""
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

    def test_english_to_french_null_input(self):
        """Test English to French Translation - Null/Blank Input"""
        self.assertEqual(translator.englishToFrench(None), 'Invalid Input')
        self.assertEqual(translator.englishToFrench(''), 'Invalid Input')

    def test_french_to_english_valid_input(self):
        """Test French to English Translation - Valid Input"""
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_french_to_english_null_input(self):
        """Test French to English Translation - Null/Blank Input"""
        self.assertEqual(translator.frenchToEnglish(None), 'Invalid Input')
        self.assertEqual(translator.frenchToEnglish(''), 'Invalid Input')


if __name__ == '__main__':
    unittest.main()
