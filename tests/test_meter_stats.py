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
        self.assertEqual(meter_count, 3)
        