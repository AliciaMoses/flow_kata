# in this class there will be the logic for integrating the console outputs defined in the console reporter class with argparse

import unittest
from unittest.mock import MagicMock, patch
from main import FlowProcessor


class TestFlowProcessor(unittest.TestCase):
    
    # use setUp hook and create mock args
    def setUp(self):
        #call MagicMock
        self.mock_args = MagicMock()
        
        # the command line utility should take a file path as an arg and then return prompts / data 
        self.mock_args.file_path = "test_file.txt"
        
        #mocking additional args to be passed in when stating command via the CLI

        self.mock_args.meters = True
        self.mock_args.valid = True
        self.mock_args.invalid = True
        self.mock_args.high_low = True
        self.mock_args.recent_old = True
        
    #calling the instanciated classes via main   
    @patch("main.FileReader")
    @patch("main.DataParser")
    @patch("main.MeterStats")
    @patch("main.ConsoleReporter")
    
    
    #define the tests
    def test_processor(self, mock_console_reporter, mock_meter_stats, mock_data_parser, mock_file_reader):
        _processor = FlowProcessor(self.mock_args)
        
        # this is calling the method to process the flow data
        _processor.process_flow()
        
        # specify the arguments that the methods are called with
        
        #this is ensuring that the file_reader instance has been given an arg of file_path
        mock_file_reader.assert_called_once_with(self.mock_args.file_path)
        
        #ensure that the read_file method has been called 
        mock_file_reader.return_value.read_file.assert_called_once()
        
        mock_data_parser.assert_called_once_with(mock_file_reader.return_value.read_file.return_value)
        mock_data_parser.return_value.parse_data.assert_called_once()

        mock_meter_stats.assert_called_once_with(mock_data_parser.return_value.parse_data.return_value)

        mock_console_reporter.assert_called_once_with(mock_meter_stats.return_value)
        mock_console_reporter.return_value.print_meter_count.assert_called_once()
        mock_console_reporter.return_value.print_sum_valid_readings.assert_called_once()
        mock_console_reporter.return_value.print_sum_invalid_readings.assert_called_once()
        mock_console_reporter.return_value.print_highest_lowest_readings.assert_called_once()
        mock_console_reporter.return_value.print_most_least_recent_readings.assert_called_once()
        
  
        
        