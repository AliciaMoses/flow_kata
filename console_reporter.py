
from meter_stats import MeterStats
# this class will require MeterStats as an arg
class ConsoleReporter():
    def __init__(self, meter_stats: MeterStats):
        self.meter_stats = meter_stats
        
    def print_meter_count(self):
        meter_count = self.meter_stats.count_meters()
        print("Count of meters:", meter_count)
        
    def print_sum_valid_readings(self):
        _sum_valid_readings = self.meter_stats.sum_valid_readings()
        print("Sum of valid meter readings:", _sum_valid_readings)
        
    def print_sum_invalid_readings(self):
        _sum_invalid_readings = self.meter_stats.sum_invalid_readings()
        print("Sum of invalid meter readings:", _sum_invalid_readings)
        
    def print_highest_lowest_readings(self):
        highest_valid_reading = self.meter_stats.highest_valid_reading()
        lowest_valid_reading = self.meter_stats.lowest_valid_reading()
        print("Highest valid meter reading:", highest_valid_reading)
        print("Lowest valid meter reading:", lowest_valid_reading)
    
    def print_most_least_recent_readings(self):
        most_recent_reading = self.meter_stats.most_recent_reading()
        least_recent_reading = self.meter_stats.least_recent_reading()
        print("Most recent meter reading:", most_recent_reading)
        print("Least recent meter reading:", least_recent_reading)