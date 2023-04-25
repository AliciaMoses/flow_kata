
from meter_stats import MeterStats
# this class will require MeterStats as an arg
class ConsoleReporter():
    def __init__(self, meter_stats: MeterStats):
        self.meter_stats = meter_stats
        
    def print_meter_count(self):
        meter_count = self.meter_stats.count_meters()
        print("Count of meters:", meter_count)