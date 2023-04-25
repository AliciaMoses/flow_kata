from file_reader import FileReader
from data_parser import DataParser
from meter_stats import MeterStats
from console_reporter import ConsoleReporter



class FlowProcessor:
    def __init__(self, args):
        self.args = args
        
    def process_flow(self):
        # file handling logic
        file_handler = FileReader(self.args.file_path)
        file_content = file_handler.read_file()
        
        
        # Transforming the data
        data_parser = DataParser(file_content)
        parsed_data = data_parser.parse_data()
        
        # Process the desired meter data
        _processor = MeterStats(parsed_data)
        
        # Output results to the console
        console_reporter = ConsoleReporter(_processor)
        
        # add logic for specific args 
        if self.args.meters:
            console_reporter.print_meter_count()
            
        if self.args.valid:
            console_reporter.print_sum_valid_readings()
            
        if self.args.invalid:
            console_reporter.print_sum_invalid_readings()
            
        if self.args.high_low:
            console_reporter.print_highest_lowest_readings()
            
        if self.args.recent_old:
            console_reporter.print_most_least_recent_readings()
            
