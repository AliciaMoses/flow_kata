# Flow Kata


## Requirements 


- file parsed into a data structure
- string values should be converted to appropriate data types
- must use argparse for the daata processing and console outputs
- must validate solution with unit tests 

Console outputs
●	The count of meters in the file
●	The total sum of valid meter readings within the file
●	The total sum of invalid meter readings within the file
●	The highest and lowest valid meter reading within the file
●	The most recent and oldest meter reading within the file


## Data 

### File Schema

HEADER |
METER | METER_ID |
READING | READING_ID | VALUE | DATE(YYYYMMDD) | STATUS (V = valid, F = Invalid) |
FOOTER |

### Converted data 
[
    { 
    METER : METER_ID, 
    READING : READING_ID,
    VALUE: FLOAT, 
    DATE: DATETIME OBJ,
    STATUS: V || F 
    }
]

## Class Design 

### Responsibilities

FileReader
- opening the file 
- reading the file's contents

DataParser
- converting data types
- saving data types to a data structure

MeterStats
- perfoming calculations to return statistics

ConsoleReporter
- deriving console outputs per function -> statistic

FlowProcessor
- handelling processing of the file with argparse / CL inputs + outputs








