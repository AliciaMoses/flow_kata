import unittest
from unittest.mock import patch

from datetime import datetime
from meter_stats import MeterStats
from console_reporter import ConsoleReporter

# this class will be responsible for console outputs from the parsed data and the meterstats class
# since there are terminal outputs to test this will require mocking and imports from the other classes 
# I will need to add in sample data so will add in a datetime import
# defining the class slightly differently 

class TestConsoleReporter(unittest.TestCase):
    
    # using this to define the data and call the MeterStats class before mocking terminal outputs in test cases
    def setUp(self):
        self.sample_data = [
            {
                "METER_ID": "METER_ID_1",
                "READING_ID": "READING_ID_1",
                "VALUE": 100.0,
                "DATE": datetime(2023, 4, 1),
                "STATUS": "V",
            },
            {
                "METER_ID": "METER_ID_1",
                "READING_ID": "READING_ID_2",
                "VALUE": 200.0,
                "DATE": datetime(2023, 4, 2),
                "STATUS": "F",
            },
            {
                "METER_ID": "METER_ID_2",
                "READING_ID": "READING_ID_3",
                "VALUE": 400.0,
                "DATE": datetime(2023, 4, 5),
                "STATUS": "V",
            },
        ]
        
        self.meter_stats = MeterStats(self.sample_data)
        self.console_reporter = ConsoleReporter(self.meter_stats)
      
    @patch('builtins.print')
    def test_print_meter_count(self, mock_print):
        self.console_reporter.print_meter_count()
        # determine the console output
        mock_print.assert_called_once_with("Count of meters:", 2)
        
    @patch('builtins.print')
    def test_print_sum_valid_readings(self, mock_print):
        self.console_reporter.print_sum_valid_readings()
        mock_print.assert_called_once_with("Sum of valid meter readings:", 500.0)

    @patch('builtins.print')
    def test_print_sum_invalid_readings(self, mock_print):
        self.console_reporter.print_sum_invalid_readings()
        mock_print.assert_called_once_with("Sum of invalid meter readings:", 200.0)
        
    # these will be printed together    
    @patch('builtins.print')
    def test_print_highest_lowest_readings(self, mock_print):
        self.console_reporter.print_highest_lowest_readings()
        # assert either is called
        mock_print.assert_any_call("Highest valid meter reading:", self.sample_data[2])
        mock_print.assert_any_call("Lowest valid meter reading:", self.sample_data[0])
        
    @patch('builtins.print')
    def test_print_most_least__recent_readings(self, mock_print):
        self.console_reporter.print_most_least_recent_readings()
        # assert either is called
        mock_print.assert_any_call("Most recent meter reading:", self.sample_data[2])
        mock_print.assert_any_call("Least recent meter reading:", self.sample_data[0])