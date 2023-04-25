import argparse
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
            
# finally need to add in main function to wrapp up the application and call argparse

def main():
    #Add in initial description to display in the console
    flow_parser = argparse.ArgumentParser(description = 'Flow File Utility')
    
    # Add in the arguments defined earlier 
    # add in help to show additional info about the arg
    
    #Making the file path optional so that you can call args that may be useful such as prompts or help
    #I am not sure if required will work but I can set the args to essentially a null value 
    flow_parser.add_argument('file_path', help="The path to the file containing the meter readings", nargs='?', default=None)
    
    flow_parser.add_argument('--meters', action="store_true", help="Show the count of meters in the file.")
    
    flow_parser.add_argument('--valid', action="store_true", help="Show the total sum of valid meter readings.")
    
    flow_parser.add_argument('--invalid', action="store_true", help="Show the total sum of invalid meter readings.")
    
    flow_parser.add_argument('--high_low', action="store_true", help="Show the highest and lowest valid meter readings")
    
    flow_parser.add_argument('--recent_old', action="store_true", help="Show the most recent and oldest meter readings")
    
    # call the module method to parse the arguments 
    
    args = flow_parser.parse_args()
    
    # add a conditional to return the help prompts if an arg is invalid 
    
    if not any([args.meters, args.valid, args.invalid, args.high_low, args.recent_old]):
        flow_parser.print_help()
        return
    
    _app = FlowProcessor(args)
    _app.process_flow()
    
if __name__ == '__main__':
    main()