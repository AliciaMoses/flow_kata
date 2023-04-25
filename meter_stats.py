from typing import List, Dict, Union
from datetime import datetime

class MeterStats():
    
    # will take argument of parsed_data
    def __init__(self, parsed_data: List[Dict[str, Union[str, float, datetime]]]):
        self.parsed_data = parsed_data
        
    # will specify that this function returns an int value
    def count_meters(self) -> int:
        return 3