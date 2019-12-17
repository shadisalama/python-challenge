import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()

    
   
    
    print(lines)
    print(type(lines))
