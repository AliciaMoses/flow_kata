import unittest
from data_parser import DataParser
from datetime import datetime


class TestDataParser(unittest.TestCase):
    def test_parse_data(self):
        content = (
            "HEADER |\n"
            "METER | METER_ID_1\n"
            "READING | READING_ID_1 | 100 | 20230401 | V |\n"
            "READING | READING_ID_2 | 200 | 20230402 | F | \n"
            "METER | METER_ID_2\n"
            "READING | READING_ID_3 | 200 | 20230405 | V |\n"
            "READING | READING_ID_4 | 500 | 20230406 | F |\n"
            "METER | METER_ID_1\n"
            "READING | READING_ID_5 | 400 | 20230405 | V |\n"
            "READING | READING_ID_6 | 600 | 20230406 | F |\n"
            "FOOTER "
        )
        
        # going to add another example to the data

        expected_data = [
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
              {
                "METER_ID": "METER_ID_1",
                "READING_ID": "READING_ID_5",
                "VALUE": 400.0,
                "DATE": datetime(2023, 4, 5),
                "STATUS": "V",
            },
            {
                "METER_ID": "METER_ID_1",
                "READING_ID": "READING_ID_6",
                "VALUE": 600.0,
                "DATE": datetime(2023, 4, 6),
                "STATUS": "F",
            },
        ]

        data_parser = DataParser(content)
        parsed_data = data_parser.parse_data()
        
        self.assertEqual(parsed_data, expected_data)

