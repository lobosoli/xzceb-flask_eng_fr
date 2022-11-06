import unittest

from translator import englishtofrench, frenchtoenglish

from ibm_cloud_sdk_core.api_exception import ApiException

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_null(self):
        with self.assertRaises(ApiException):
            englishtofrench("")

    def test_frenchToEnglish_null(self):
        with self.assertRaises(ApiException):
            frenchtoenglish("")

    def test_englishToFrench(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()
