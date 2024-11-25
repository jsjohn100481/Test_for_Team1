import unittest
from unittest.mock import patch
from fourth_analysis import FourthAnalysis
from model import Issue

class TestFourthAnalysis(unittest.TestCase):

    @patch('fourth_analysis.DataLoader')
    def test_valid_dataset(self, MockDataLoader):
      
        mock_issues = [
            Issue(jobj={"number": 1, "created_date": "2022-05-01", "state": "open"}),
            Issue(jobj={"number": 2, "created_date": "2022-06-15", "state": "closed"}),
            Issue(jobj={"number": 3, "created_date": "2023-07-20", "state": "open"}),
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = FourthAnalysis()
        with patch('matplotlib.pyplot.show'): 
            analysis.run()

        self.assertTrue(True)

    @patch('fourth_analysis.DataLoader')
    def test_empty_dataset(self, MockDataLoader):
      
     
        MockDataLoader.return_value.get_issues.return_value = []

        analysis = FourthAnalysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('fourth_analysis.DataLoader')
    def test_invalid_dates(self, MockDataLoader):
       
        mock_issues = [
            Issue(jobj={"number": 1, "created_date": None, "state": "open"}),
            Issue(jobj={"number": 2, "created_date": "invalid-date", "state": "closed"}),
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = FourthAnalysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('fourth_analysis.DataLoader')
    def test_single_year_dataset(self, MockDataLoader):

        mock_issues = [
            Issue(jobj={"number": 1, "created_date": "2022-01-01", "state": "open"}),
            Issue(jobj={"number": 2, "created_date": "2022-12-31", "state": "closed"}),
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = FourthAnalysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('fourth_analysis.DataLoader')
    def test_large_dataset(self, MockDataLoader):
  
        mock_issues = [
            Issue(jobj={"number": i, "created_date": f"2022-01-{i % 30 + 1:02d}", "state": "open"})
            for i in range(1000)
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = FourthAnalysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()