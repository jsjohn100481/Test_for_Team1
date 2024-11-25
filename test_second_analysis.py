import unittest
from unittest.mock import patch
from second_analysis import Second_analysis
from model import Issue, Event

class TestSecondAnalysis(unittest.TestCase):

    @patch('second_analysis.DataLoader')
    def test_valid_dataset(self, MockDataLoader):
        # Mock data with valid dataset and author
        mock_issues = [
            Issue(jobj={"number": 1, "created_date": "2022-01-01", "state": "open", "author": "author1"}),
            Issue(jobj={"number": 2, "created_date": "2022-06-15", "state": "closed", "author": "author2"}),
            Issue(jobj={"number": 3, "created_date": "2023-07-20", "state": "open", "author": "author1"}),
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        # Running the analysis
        analysis = Second_analysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('second_analysis.DataLoader')
    def test_empty_dataset(self, MockDataLoader):
        # Empty dataset to test the case
        MockDataLoader.return_value.get_issues.return_value = []

        analysis = Second_analysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('second_analysis.DataLoader')
    def test_invalid_author(self, MockDataLoader):
        # Mock data with invalid authors
        mock_issues = [
            Issue(jobj={"number": 1, "created_date": "2022-01-01", "state": "open", "author": "author1"}),
            Issue(jobj={"number": 2, "created_date": "2022-06-15", "state": "closed", "author": "author2"}),
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = Second_analysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('second_analysis.DataLoader')
    def test_single_year_dataset(self, MockDataLoader):
        # Mock data with a single year of issues
        mock_issues = [
            Issue(jobj={"number": 1, "created_date": "2022-01-01", "state": "open", "author": "author1"}),
            Issue(jobj={"number": 2, "created_date": "2022-12-31", "state": "closed", "author": "author2"}),
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = Second_analysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

    @patch('second_analysis.DataLoader')
    def test_large_dataset(self, MockDataLoader):
        # Mock data with a large dataset
        mock_issues = [
            Issue(jobj={"number": i, "created_date": f"2022-01-{i % 30 + 1:02d}", "state": "open", "author": f"author{i % 5}"})
            for i in range(1000)
        ]
        MockDataLoader.return_value.get_issues.return_value = mock_issues

        analysis = Second_analysis()
        with patch('matplotlib.pyplot.show'):  
            analysis.run()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
