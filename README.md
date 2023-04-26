# Flow Kata

## Instructions 

In the terminal, navigate to the project directory 

```bash
 ~$ cd flow_kata
```

Run the program with the following command

```bash
 ~$ python main.py
```

The following prompts will be shown in the terminal:

```bash
usage: main.py [-h] [--meters] [--valid] [--invalid] [--high_low] [--recent_old] [file_path]

Flow File Utility

positional arguments:
  file_path     The path to the file containing the meter readings

options:
  -h, --help    show this help message and exit
  --meters      Show the count of meters in the file.
  --valid       Show the total sum of valid meter readings.
  --invalid     Show the total sum of invalid meter readings.
  --high_low    Show the highest and lowest valid meter readings
  --recent_old  Show the most recent and oldest meter readings
```


Enter a file path and then add an additional argument to return information from the file

```bash
 ~$ python main.py data/data.txt --meters

Count of meters: 3

```

## Tests

Tests are in the /tests subdirectory and can be run with the following terminal command:

```bash
 ~$ python -m unittest discover
```



## Requirements 


- file parsed into a data structure
- string values should be converted to appropriate data types
- must use argparse for the daata processing and console outputs
- must validate solution with unit tests 

Console outputs
- The count of meters in the file
- The total sum of valid meter readings within the file
- The total sum of invalid meter readings within the file
- The highest and lowest valid meter reading within the file
- The most recent and oldest meter reading within the file


## Data 

### File Schema

The original file schema is as follows:

HEADER |
METER | METER_ID |
READING | READING_ID | VALUE | DATE(YYYYMMDD) | STATUS (V = valid, F = Invalid) |
FOOTER |

### Converted data 

The data types used are strings by default, unless stated otherwise


[
    { 
    METER : METER_ID, 
    READING : READING_ID,
    VALUE: FLOAT, 
    DATE: DATETIME OBJ,
    STATUS: V || F 
    }
]

Owing to the requirements for consaole outputs, the data structure used for the parsed data is a list of dictionaries for each reading and its corresponding meter
This allows for the dictionaries to be iterated over with list comprehensions and simplifies the functions and tests required for outputting the desired stats

## Class Design 

### Responsibilities

To adhere to SOLID principles, the functions of the program have been segregated into classes, each with a single, primary responsibility


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


## NB

The typing module has been used in this project to ensure the correct data types are used and the correct values / data strcutures / objects are returned 
It has also been used to improve readability





