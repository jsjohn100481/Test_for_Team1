import unittest
from first_analysis import FirstAnalysis


class testFirstAnalysis(unittest.TestCase):
    def test_run(self):
        result = FirstAnalysis.run(self)
        expected_result = None
        self.assertEqual(result, expected_result)
        
    def test_categorize_key(self):
        key = "Author"
        result = FirstAnalysis.categorize_key(key)
        expected_result = 'A'
        self.assertEqual(result, expected_result)
        