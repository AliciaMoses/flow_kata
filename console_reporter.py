
from meter_stats import MeterStats
# this class will require MeterStats as an arg
class ConsoleReporter():
    def __init__(self, meter_stats: MeterStats):
        self.meter_stats = meter_stats
        
    def print_meter_count(self):
        meter_count = self.meter_stats.count_meters()
        print("Count of meters:", meter_count)
        
    def print_sum_valid_readings(self):
        meter_count = self.meter_stats.sum_valid_readings()
        print("Sum of valid meter readings:", meter_count)
        
    def print_sum_invalid_readings(self):
        meter_count = self.meter_stats.sum_invalid_readings()
        print("Sum of invalid meter readings:", meter_count)