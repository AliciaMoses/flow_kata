from typing import List, Dict, Union
from datetime import datetime

class MeterStats():
    
    # will take argument of parsed_data
    def __init__(self, parsed_data: List[Dict[str, Union[str, float, datetime]]]):
        self.parsed_data = parsed_data
        
    # will specify that this function returns an int value
    
    def count_meters(self) -> int:
        #create a set using METER_ID key, since it will handle the issue of duplicates
        # simply return the length of the set
        return len(set([data["METER_ID"] for data in self.parsed_data]))
    
    def sum_valid_readings(self) -> float:
        return sum([data["VALUE"] for data in self.parsed_data if 
                    isinstance(data["VALUE"], (int, float)) and data["STATUS"] == "V"])
    
    def sum_invalid_readings(self) -> float:
         return sum([data["VALUE"] for data in self.parsed_data if 
                    isinstance(data["VALUE"], (int, float)) and data["STATUS"] == "F"])
    
    