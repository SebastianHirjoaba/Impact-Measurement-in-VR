# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:20:08 2023

@author: Sebastian Hirjoaba
"""

import csv
import os
filename = '11111.csv' 
tags = ['_Painting','_Text']

output_file = "output_file.csv"
new_file = []
headers = ["Timestamp","Object","Distance","Coordinates_x","Coordinates_y","Coordinates_z","Type"]
new_file.append(headers)


with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        thing = row[1]
        if "Painting" in thing:
            tag = "Painting"
            row.append(tag)
            for token in tags:
                if token in thing:
                   row[1] = row[1].replace(token, '')
            new_file.append(row)
        elif "Text" in thing:
            tag = "Text"
            row.append(tag)
            for token in tags:
                if token in thing:
                   row[1] = row[1].replace(token, '')
            new_file.append(row)
            
with open('sebi_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_file)
