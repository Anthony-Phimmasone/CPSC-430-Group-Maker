# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:26:05 2019

@author: phimm_000
"""

import os

#Group Maker
#Anthony Phimmasone
#Denzel Saraka
#Igor Asipenka
#James Donahue

import pandas as pd

#Ask the user to enter in a CSV filename
filename = input("Enter a filename: ")

#While the file does not exist
#Ask the user to re-enter filename
#The path of the file
while not os.path.exists('./' + filename):
    print("File does not exist or incorrect spelling")
    filename = input("Enter a filename: ")

#Print the CSV file
df = pd.read_csv(filename)
print(df)

#Write to the CSV
file = open('GroupMakerOutput.csv', "w")
#df.to_csv(index=False)
print("Successfully wrote to output file!")