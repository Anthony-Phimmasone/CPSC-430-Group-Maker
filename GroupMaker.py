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


def ansToBool(answer):
    if(answer == "Y" or answer == "y"):
        return True

    else:
        return False



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


groupInput = " "
while(1):
    groupInput = input("How would you like to have your groups created?\nBy number of students per group[N]?\nOr\nBy how many groups will be made[G]\n")
    if(groupInput == "G" or groupInput == "N"):
        break

if(groupInput == "N"):
    numStud = input("How many students per group?")

if(groupInput == "G"):
    numGroup = input("How many groups will be made?")

#Menu:

#random bool
randBool = ansToBool(input("Would you like the groups to be completely randomized? [Y/N]"))
print(randBool)

#if the user wants options
if(not randBool):
    #blacklist bool
    blackBool = ansToBool(input("Would you like to use the blacklist? [Y/N]"))

    #gender bool
    genBool = ansToBool(input("Would you like to create groups based on gender? [Y/N]"))

    #preferred bool
    prefBool = ansToBool(input("Would you like to include student group preferences? [Y/N]"))

    #personality bool
    persBool = ansToBool(input("Would you like to create groups based on personality? [Y/N]"))


#Write to the CSV
df.to_csv('GroupMakerOutput.csv')
print("Successfully wrote to output file!")











