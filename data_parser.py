# I will be using the typing module here for consistency and readability

from typing import List, Dict, Union
from datetime import datetime

class DataParser():
    def __init__(self, content: str):
        self.content = content
        
    # using typing to define the correct data types and structure 
    # the structure is a list of dictionaries with strings, float val and datetime object   
    def parse_data(self) -> List[Dict[str, Union[str, float, datetime]]]:
        
        # now need to initialise an empty list for the data
        
        parsed_data = []
        
        # split the main string (within the file) up by line
        lines = self.content.split('\n')
        
        # iterate over the lines
        
        for line in lines:
            #skip over empty lines, header and footer
            if line.startswith("HEADER") or line.startswith("FOOTER") or not line.strip():
                continue
            
            # create fields from the line
            fields = line.split("|")
            
            # extract data from fields
            record_type = fields[0].strip()
            
            if record_type == "METER":
                # Define as meter_id
                meter_id = fields[1].strip()
                # taking the next value and saving that as a variable called meter_id
            elif record_type == "READING":
                reading_id = fields[1].strip()
                # define this as type float, since the others were str by default
                value = float(fields[2].strip())
                date_str = fields[3].strip()
                status = fields[4].strip()
                
                # convert date_str into the datetime object
                date = datetime.strptime(date_str, "%Y%m%d")
                
                # add the parsed data to the list of dictionaries
                
                parsed_data.append({
                    "METER_ID": meter_id,
                    "READING_ID": reading_id,
                    "VALUE": value,
                    "DATE": date,
                    "STATUS": status  
                })
        
        return parsed_data 