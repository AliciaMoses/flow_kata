import unittest
from datetime import datetime
from meter_stats import MeterStats

class TestMeterStats(unittest.TestCase):
    
    data =     [
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
                "VALUE": 200.0,
                "DATE": datetime(2023, 4, 5),
                "STATUS": "V",
            },
            {
                "METER_ID": "METER_ID_2",
                "READING_ID": "READING_ID_4",
                "VALUE": 500.0,
                "DATE": datetime(2023, 4, 6),
                "STATUS": "F",
            },
    ]
    
    def test_count_meters(self):
        meter_stats = MeterStats(self.data)
        meter_count = meter_stats.count_meters()
        self.assertEqual(meter_count, 2) # Corrected the assertion statement, should have been 2 previously
        
    def test_sum_valid_readings(self):
        meter_stats = MeterStats(self.data)
        _sum = meter_stats.sum_valid_readings()
        self.assertEqual(_sum, 300.0)
    
    def test_sum_invalid_readings(self):
        meter_stats = MeterStats(self.data)
        _sum = meter_stats.sum_invalid_readings()
        self.assertEqual(_sum, 700.0)
        
    # Need to pass in the specific key
   
    def test_highest_valid_reading(self):
        meter_stats = MeterStats(self.data)
        highest = meter_stats.highest_valid_reading()
        self.assertEqual(highest["VALUE"], 200.0)
    
     
    def test_lowest_valid_reading(self):
        meter_stats = MeterStats(self.data)
        lowest = meter_stats.lowest_valid_reading()
        self.assertEqual(lowest["VALUE"], 100.0)
    

    def test_most_recent_reading(self):
        meter_stats = MeterStats(self.data)
        most_recent = meter_stats.most_recent_reading()
        self.assertEqual(most_recent["READING_ID"], "READING_ID_4")
    
    # corrected error in test function name here

    def test_least_recent_reading(self):
        meter_stats = MeterStats(self.data)
        least_recent = meter_stats.least_recent_reading()
        self.assertEqual(least_recent["READING_ID"], "READING_ID_1")