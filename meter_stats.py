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
    
    # For this method I will be returning a dictionary with the specified data types within it
    def highest_valid_reading(self) -> Dict[str, Union[str, float, datetime]]:
        # Define valid readings(same logic as before)
        valid_readings = [data for data in self.parsed_data if data["STATUS"] == "V"]
        # return the max value from above
        # Here I need to use a hidden function to handle accessing the correct key
        return max(valid_readings, key=lambda x: x["VALUE"])
    
      # For this method I will be returning a dictionary with the specified data types within it
    def lowest_valid_reading(self) -> Dict[str, Union[str, float, datetime]]:
        # Define invalid readings(same logic as before)
        valid_readings = [data for data in self.parsed_data if data["STATUS"] == "V"]
        # return the min value from above
        # Here I need to use a hidden function to handle accessing the correct key
        return min(valid_readings, key=lambda x: x["VALUE"])
    
    