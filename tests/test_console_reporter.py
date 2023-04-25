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
        return super().setUp()
