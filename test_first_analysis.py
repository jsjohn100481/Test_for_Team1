from unittest import TestCase, mock
from first_analysis import FirstAnalysis


class TestFirstAnalysis(TestCase):
    
    @mock.patch('config.get_parameter', return_value='test_user')
    def test_initialization(self, mock_get_parameter):
        analysis = FirstAnalysis()
        self.assertEqual(analysis.USER, 'test_user')

    def test_categorize_key(self):
        def categorize_key(key):
            if not key:
                return 'Other'  # Handle empty strings
            elif 'A' <= key[0] <= 'G':
                return 'A-G'
            elif 'H' <= key[0] <= 'N':
                return 'H-N'
            elif 'O' <= key[0] <= 'T':
                return 'O-T'
            elif 'U' <= key[0] <= 'Z':
                return 'U-Z'
            else:
                return 'Other'

        self.assertEqual(categorize_key(""), 'Other')
        self.assertEqual(categorize_key("Aardvark"), 'A-G')
        self.assertEqual(categorize_key("Monkey"), 'H-N')
        self.assertEqual(categorize_key("Turtle"), 'O-T')
        self.assertEqual(categorize_key("Umbrella"), 'U-Z')

    @mock.patch('first_analysis.DataLoader')
    def test_author_event_counting(self, mock_data_loader):
        # Mock events with various authors and event types
        mock_events = [
            mock.Mock(author='Alice', event_type='Commit'),       # A-G
            mock.Mock(author='Bob', event_type='Pull Request'),  # A-G
            mock.Mock(author='Charlie', event_type='Comment'),   # A-G
            mock.Mock(author='Helen', event_type='Merge'),       # H-N
            mock.Mock(author='Nancy', event_type='Commit'),      # H-N
            mock.Mock(author='Oscar', event_type='Issue'),       # O-T
            mock.Mock(author='Tom', event_type='Review'),        # O-T
            mock.Mock(author='Uma', event_type='Comment'),       # U-Z
            mock.Mock(author='Zoe', event_type='Commit'),        # U-Z
            mock.Mock(author='123Author', event_type='Tag'),     # Other
            mock.Mock(author=None, event_type='Unknown'),        # No author
        ]

        # Mock issues containing these events
        mock_issue1 = mock.Mock(events=mock_events[:5])  # First issue
        mock_issue2 = mock.Mock(events=mock_events[5:])  # Second issue
        mock_data_loader.return_value.get_issues.return_value = [mock_issue1, mock_issue2]

        # Run analysis
        analysis = FirstAnalysis()
        with mock.patch('builtins.input', side_effect=['1', '1', 'Alice']), \
            mock.patch('builtins.print') as mock_print:
            analysis.run()

        # Assertions
        for call in mock_print.mock_calls:
            print(call)
