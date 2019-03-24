# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:26:05 2019
@author: phimm_000
"""

#Group Maker
#Anthony Phimmasone
#Denzel Saraka
#Igor Asipenka
#James Donahue

import os
import random
import math
import csv

def ansToBool(answer):
    if(answer == "Y" or answer == "y"):
        return True

    else:
        return False

#Ask the user to enter in a CSV filename
filename = input("Enter a filename (include the .csv): ")

#While the file does not exist
#Ask the user to re-enter filename
#The path of the file
while not os.path.exists('./' + filename):
    print("File does not exist or incorrect spelling")
    filename = input("Enter a filename (include the .csv): ")

students = []
with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        students.append(row)

nameList = []
for row in students:
    nameList.append(row['Name'])

'''
#Get all the information in the column based on the Header name
nameList = list(df['Name'])
preferredList = list(df['Preferred List'])
blackList = list(df['Blacklist'])
personalityList = list(df['Personality Type'])
genderList = list(df['Gender'])
skillsList = list(df['Programming Skills'])
'''

#Creates lists for each row and puts it into a list (AKA lists of lists)
#listOflists = df.values.tolist()

#Randomize the list
random.shuffle(nameList)
#random.shuffle(listOflists)
print(nameList)
print("\n\n\n")
#print(listOflists)
#print("\n\n\n")

numStud = " "
numGroup = " "
groupInput = " "
while(1):
    groupInput = input("How would you like to have your groups created?\nBy number of students per group[N]?\nOr\nBy how many groups will be made[G]\n")
    if(groupInput == "G" or groupInput == "N"):
        break

result = []
if(groupInput == "N"):
    numStud = input("How many students per group?")
    i = -1
    for j in range(len(nameList)):
        if j % int(numStud) == 0:
            result.append([])
            i = i + 1
        result[i].append(nameList[j])

if(groupInput == "G"):
    numGroup = input("How many groups will be made?")
    perGroup = math.ceil(len(nameList) / int(numGroup))
    i = -1
    for j in range(len(nameList)):
        if j % int(perGroup) == 0:
            result.append([])
            i = i + 1
        result[i].append(nameList[j])
'''
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
'''

#df = pd.DataFrame.from_records(result)
#print(df)
#Write to the CSV
#df.to_csv('GroupMakerOutput.csv')

with open('GroupMakerOutput.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in result:
        csv_writer.writerow(row)
print("Successfully wrote to output file!")
