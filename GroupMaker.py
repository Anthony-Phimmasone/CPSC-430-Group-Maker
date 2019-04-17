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
import datetime
import numpy as np
import pandas as pd

def printTitle():
    print("   ______                          __  ___      __            ")
    print("  / ____/________  __  ______     /  |/  /___ _/ /_____  _____")
    print(" / / __/ ___/ __ \/ / / / __ \   / /|_/ / __ `/ //_/ _ \/ ___/")
    print("/ /_/ / /  / /_/ / /_/ / /_/ /  / /  / / /_/ / ,< /  __/ /    ")
    print("\____/_/   \____/\__,_/ .___/  /_/  /_/\__,_/_/|_|\___/_/     ")
    print("                     /_/                                      ")

def printOutput(result, randStudents,headers):
    for i in range(len(result)):
        for j in range(0, len(result[i])):
            if(j ==0):
                print("Group", result[i][j], ": ", end = "\n", sep = "")
                print("|"," ".join(headers),"|")
                print("___________________________________")
            else:
                student = result[i][j]
                #print(student)
                index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
                #print(index)
                studRow = randStudents.iloc[index].values
                studRow = list(studRow)
                studRow = [' ' if x is np.nan else x for x in studRow]
                print("|"," ".join(studRow),"|")
                #print(studRow)
                print("___________________________________")
        print("\n\n")


def genRand(nameList, numStud, numGroup, groupInput):
    #creating totally randomized groups
    result = []
    remainder = 0
    if groupInput.upper() == "N":
        remainder = len(nameList) % int(numStud)
        if not remainder == 0:
            print("Groups may have extra students")
    leftOver = []
    i = -1
    for j in range(len(nameList) - remainder):
        #creates a list
        if j % int(numStud) == 0:
            i = i + 1
            if groupInput.upper() == "G" and i >= numGroup:
                leftOver = nameList[j:]
                break
            result.append([i])
        result[i].append(nameList[j])
    if groupInput.upper() == "N":
        leftOver = nameList[len(nameList) - remainder:]
    k = 0
    for i in range(len(leftOver)):
        if k == len(result):
            k = 0
        result[k].append(leftOver[i])
        k = k + 1

    return result


def blacklist(nameList, numStud, numGroup, randStudents, groupInput, possResult):
    if(len(possResult)==0):
        result = []
        result = genRand(nameList,numStud,numGroup,groupInput)
    else:
        result = possResult
    
    totalAttempts = 0
    #pop off numbers in the beginning
    for i in range(len(result)):
        result[i].pop(0)
    readyBool = False
    print("Result: ",result)
    
    totalGroups= len(result)
    while(not readyBool):
        #check that students are not in a group with their blacklistee
        for groupnum in range(len(result)):
            group = result[groupnum]
            for studentnum in range(len(group)):
                student = group[studentnum]
                index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
                #print(index)
                blackValue = randStudents.at[index,"Blacklist"]
                #print(student ," does not want to pair with: ",blackValue)
                if(str(blackValue) == 'nan'):
                    continue
                else:
                    #check if blacklistee in students group
                    if blackValue in group:
                        randGroup = random.randint(0,totalGroups-1)
                        while randGroup == groupnum:
                            randGroup = random.randint(0,totalGroups-1)
                        
                        randStud = random.randint(0,len(result[randGroup])-1)
                        
                        #get and remove students that need to move
                        studToMove = result[randGroup].pop(randStud)
                        currStud = result[groupnum].pop(studentnum)
                        #print("Random Student Selected is:", studToMove)
                        #print("Current Student Selected is:", currStud)
                        #insert STM to current list
                        result[groupnum].insert(studentnum,studToMove)
                        #print("STM moved to group "+str(randGroup)+" position "+str(randStud))
                        
                        #insert currStud to rand group
                        result[randGroup].insert(randStud,currStud)
                        #print("CurrStud moved to group "+str(groupnum)+" position "+str(studentnum))
                        #print("Result: ",result)
                        

        #check if groups are complete
        foundError = False
        for groupnum in range(len(result)):
            group = result[groupnum]
            totalAttempts +=1
            if(totalAttempts >= 1000):
                print("Blacklist option may be impossible, best attempt used.")
                readyBool = True
                break
            
            for student in group:
                index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
                blackValue = randStudents.at[index,"Blacklist"]
                if str(blackValue) in group:
                    readyBool = False
                    foundError = True
                elif str(blackValue) not in group:
                    if(groupnum == len(result) -1) and group.index(student) == len(group)-1 and not foundError:
                        #print("groups are complete!")
                        readyBool = True
                        
    #add numbers to beginning of groups
    for i in range(len(result)):
        result[i].insert(0,i)

    return result


def customChoiceSame(nameList, numStud, numGroup, randStudents, category):
    result = []
    remainder = 0
    if not remainder == 0:
        print("Groups may have extra students")

    #i = 0
    groupValue=''
    leftOver = []
    if numGroup == " ":
        totalGroups=(len(nameList)-remainder)/int(numStud)
        leftOver = nameList[len(nameList) - remainder:]
        remainder = len(nameList) % int(numStud)
    else:
        i = -1
        for j in range(len(nameList) - remainder):
            #creates a list
            if j % int(numStud) == 0:
                i = i + 1
                if groupInput.upper() == "G" and i >= numGroup:
                    leftOver = nameList[j:]
                    break
        totalGroups = int(numGroup)
        remainder = int(len(leftOver))
        
    print("leftover:")
    print(leftOver)
    catList=randStudents[category].tolist()
    uniqueCat=[]
    for x in catList:
        if x not in uniqueCat:
            uniqueCat.append(x)
    
    #create groups
    for x in range(int(totalGroups)):
        result.append([])
        if x<len(uniqueCat):
            result[x].append(uniqueCat[x])
        else:
            result[x].append("extra")
    
    print(result)
    print("Number of students: "+str(numStud))
    print("Number of Groups: "+str(numGroup))
    
    
    for j in range(0,len(nameList)-remainder):
        student = nameList[j]
        index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
            #print(index)
        groupValue = randStudents.at[index,category]
        print(student, " value is : ",groupValue)
        for k in range(int(totalGroups)):
            #print("group search number is:",str(k))
            if not len(result[k])==int(numStud)+1 and groupValue in result[k]:
                print(student," placed in group ",str(k))
                result[k].append(student)
                break
            elif k==int(totalGroups)-1:
                #find random group with space and put student in there
                rand=random.randint(0,int(totalGroups)-1)
                print("locating random group, randnum is:",rand)
                while len(result[rand]) == int(numStud)+1:
                    rand=random.randint(0,int(totalGroups)-1)
                print("locating random group, randnum is:",rand)
                print(student, " Placed in group ", str(rand))  
                result[rand].append(student)
                break
    print("Method groups")
    print(result)
 
    '''
    leftOver = nameList[len(nameList) - remainder:]
    print(leftOver)
    '''
    for i in range(len(leftOver)):
        student = leftOver[i]
        #print("Leftover Student:",student)
        index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
            #print(index)
        groupValue = randStudents.at[index,category]
        for x in range(0,int(totalGroups)):
            if groupValue in result[x]:
                result[x].append(student)
                #print("placed in: ",result[x])
                break
            elif x==totalGroups-1:
                rand=random.randint(0,totalGroups-1)
                while len(result[rand]) == int(numStud)+2:
                    rand=random.randint(0,totalGroups-1)

                #print("placed in: ",result[rand])
                result[rand].append(student)

    for i in range(len(result)):
        result[i].pop(0)
        result[i].insert(0,i)
    #print(result)
    return result


def uniqCat(groupList,randStudents,category):
    uniqueCat=[]
    for person in groupList:
        student = person
        index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
            #print(index)
        studCat = randStudents.at[index,category]
        if studCat not in uniqueCat:
            uniqueCat.append(studCat)
     
    return uniqueCat

def customChoiceDif(nameList, numStud, numGroup, randStudents, category):
    result = []
    remainder = 0
    if not remainder == 0:
        print("Groups may have extra students")


    leftOver = []
    if numGroup == " ":
        totalGroups=(len(nameList)-remainder)/int(numStud)
        leftOver = nameList[len(nameList) - remainder:]
        remainder = len(nameList) % int(numStud)
    else:
        i = -1
        for j in range(len(nameList) - remainder):
            #creates a list
            if j % int(numStud) == 0:
                i = i + 1
                if groupInput.upper() == "G" and i >= numGroup:
                    leftOver = nameList[j:]
                    break
        totalGroups = int(numGroup)
        remainder = int(len(leftOver))
        
    #create empty groups
    for x in range(int(totalGroups)):
        result.append([])

    for j in range(0,len(nameList)-remainder):
        student = nameList[j]
        index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
            #print(index)
        studCat = randStudents.at[index,category]
        #print(student, " value is : ",studCat)
        for k in range(int(totalGroups)):
            #print("group search number is:",str(k))
            #group is empty
            if len(result[k])==0:
                result[k].append(student)
                #print(student, "1st placed into group",str(k))
                break
            
            groupVals = uniqCat(result[k],randStudents,category)
            if studCat not in groupVals and not len(result[k])==int(numStud):
                #print(student, "placed into group",str(k))
                result[k].append(student)
                break
            
            elif k==totalGroups-1:
                rand=random.randint(0,totalGroups-1)
                while len(result[rand]) == int(numStud):
                    rand=random.randint(0,totalGroups-1)

                #print(student, "placed into group",str(k))
                result[rand].append(student) 
                break
            
    #print("Method groups")
    #print(result)
 
     
    leftOver = nameList[len(nameList) - remainder:]
    print(leftOver)
    for i in range(len(leftOver)):
        student = leftOver[i]
        #print("Leftover Student:",student)
        index = randStudents[randStudents['Name']==student].index.values.astype(int)[0]
            #print(index)
        studCat = randStudents.at[index,category]
        for x in range(0,int(totalGroups)):
            groupVals = uniqCat(result[k],randStudents,category)
            if studCat not in groupVals:
                result[k].append(student)
                break
            
            elif x==totalGroups-1:
                rand=random.randint(0,totalGroups-1)
                while len(result[rand]) == int(numStud)+1:
                    rand=random.randint(0,totalGroups-1)

                #print("placed in: ",result[rand])
                result[rand].append(student) 
                break
            
    for i in range(len(result)):
        result[i].insert(0,i)
    #print(result)
    return result


def ansToBool(answer):
    if(answer == "Y" or answer == "y"):
        return True

    else:
        return False

def ansToSorD(answer):
    #if Same then true else false
    if(answer == "S" or answer == "s"):
        return True

    else:
        return False

randBool = False



#print Title
printTitle()




#Ask the user to enter in a CSV filename
#filename = input("Enter a filename (include the .csv): ")
#User can enter in a filename with or without the .csv
print("Enter in a filename with the .csv")
filename = input("Enter a filename: ")
#If a filename is not shorter than 5 character and does not end with .csv
#Then concatenate the .csv to the end of the filename
while True:
    if not filename.strip().endswith(".csv"):
        print("Please enter a proper CSV filename with the .csv extension!")
        filename = input("Enter a filename: ")
    else:
        break
#print(filename)

#While the file does not exist
#Ask the user to re-enter filename
#The path of the file
while not os.path.exists('./' + filename):
    print("File does not exist or incorrect spelling")
    filename = input("Enter a filename (include the .csv): ")

#total csv file
totalDF = pd.read_csv(filename)
#print successfully read csv
print("Successfully read csv file")
print(totalDF)
'''
students = []
with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        students.append(row)
'''
#copy first header row to headers list
headers = list(totalDF.columns.values)
#totalDF.drop(totalDF.index[0])

#print("headers\n")
#print(headers)

#shuffle rows
randStudents= totalDF.sample(frac=1)
#print("Student List:\n")
#print(randStudents)

#create list of names
nameList = randStudents['Name'].values

#TODO: Check if file has extra headers

#Get all the information in the column based on the Header name
#for i in range(3, len (headers))
#categoryOne = headers[2]
#categoryTwo = headers[3]
#categoryThree = headers[4]
#print(categoryOne)
#print(categoryTwo)
#print(categoryThree)




category1=''
category2=''
category3=''
for i in range(1, len (headers)):
    if i==2:
        category1=headers[2]
    if i==3:
        category2=headers[3]
    if i==4:
        category3=headers[4]
'''
print(category1)
print(category2)
print(category3)
'''


#Creates lists for each row and puts it into a list (AKA lists of lists)
#listOflists = df.values.tolist()

print("\n\n\n")


#TODO:
#Or if the user only wants one group then ignore options and export random list
#how to fix, xet randBool to True; if (randbool): dont ask for randool input

numStud = " "
numGroup = " "
groupInput = " "
while(1):
    groupInput = input("How would you like to have your groups created?\nBy number of students per group[N]?:\nOr\nBy how many groups will be made[G]:\n")
    if(groupInput.upper() == "G" or groupInput.upper() == "N"):
        break

#Check if students in group is excedes maximum

if(groupInput.upper() == "N"):
    while True:
        numStud = input("How many minimum students per group?")
        #If the input entered is not a number or is longer than the amount of students
        #Then it is invalid
        '''
       # tempMod = len(nameList) % int(numStud)
        if not tempMod == 0:
            if tempMod < int(numStud):
                # int(numStud)/2
                print("Invalid Input!")
'''
        if not numStud.isdigit() or int(numStud) > len(nameList) or int(numStud) == 0:
            print("Invalid Input!")
        elif len(nameList) == int(numStud):
            randBool = True
            break
        elif int(numStud)*2 > len(nameList):
            print("Minimum Students in groups too large, please try a lower number")

        else:
            break


if(groupInput.upper() == "G"):
    while True:
        numGroup = input("How many groups will be made?")
        #numStud = int(math.floor(len(nameList) / int(numGroup)))
        if not numGroup.isdigit() or int(numGroup) == 0 or int(numGroup) > len(nameList):
            print("Invalid Input!")
        else:
            numGroup = int(numGroup)
            numStud = int(math.floor(len(nameList) / numGroup))
            if int(numGroup) == 1:
                randBool = True
                #print(randBool)
            break


#Menu:

blackBool = False

categoryOneBool = False
categoryTwoBool = False
categoryThreeBool = False

#random bool
if not randBool:
    randBool = ansToBool(input("Would you like the groups to be completely randomized? [Y/n]: "))
#TODO: Make sure if 8 groups and 10 students makes 8 groups instead of 10

if randBool:
    result = []
    result = genRand(nameList,numStud,numGroup,groupInput)


#if the user wants options
if not randBool:
    #blacklist bool
    blackBool = ansToBool(input("Would you like to use the blacklist? [Y/n]: "))


if not category1=='' and not randBool:
    categoryOneText = "Would you like to create groups based on " + category1 + "? [Y/n]: "
    categoryOneBool = ansToBool(input(categoryOneText))
    if categoryOneBool:
        category1choice=ansToSorD(input("Should groups have similar values or different values? [S/D]:"))
        print(category1choice)

if not category2=='' and not categoryOneBool and not randBool:
    categoryTwoText = "Would you like to create groups based on " + category2 + "? [Y/n]: "
    categoryTwoBool = ansToBool(input(categoryTwoText))
    if categoryTwoBool:
        category2choice=ansToSorD(input("Should groups have similar values or different values? [S/D]:"))
        print(category2choice)

if not category3=='' and not categoryOneBool and not categoryTwoBool and not randBool:
    categoryThreeText = "Would you like to create groups based on " + category3 + "? [Y/n]: "
    categoryThreeBool = ansToBool(input(categoryThreeText))
    if categoryThreeBool:
        category3choice=ansToSorD(input("Should groups have similar values or different values? [S/D]:"))
        print(category3choice)
    

#category1 choice
if categoryOneBool:
    #run custom method here
    result=[]
    if category1choice:
        result = customChoiceSame(nameList, numStud, numGroup, randStudents, category1)
    if not category1choice:
        result=customChoiceDif(nameList, numStud, numGroup, randStudents, category1)
        
#category2 choice
if categoryTwoBool:
    #run custom method here
    result=[]
    if category2choice:
        result = customChoiceSame(nameList, numStud, numGroup, randStudents, category2)
    if not category2choice:
        result=customChoiceDif(nameList, numStud, numGroup, randStudents, category2)
        
#category3 choice
if categoryThreeBool:
    #run custom method here
    result=[]
    if category3choice:
        result = customChoiceSame(nameList, numStud, numGroup, randStudents, category3)
    if not category3choice:
        result=customChoiceDif(nameList, numStud, numGroup, randStudents, category3)

#user selected just blacklist option
if blackBool and not categoryOneBool and not categoryTwoBool and not categoryThreeBool:
    result=[]
    empty = []
    result=blacklist(nameList,numStud,numGroup,randStudents,groupInput,empty)

#user selected blacklist and a category
if ((blackBool and categoryOneBool) or (blackBool and categoryTwoBool) or (blackBool and categoryThreeBool)):
    result=blacklist(nameList,numStud,numGroup,randStudents,groupInput,result)

print("\n\n")


if randBool == False and blackBool == False and categoryOneBool == False and categoryTwoBool == False and categoryThreeBool == False:
    randBool = True
    result = []
    result = genRand(nameList,numStud,numGroup,groupInput)

#df = pd.DataFrame.from_records(result)
#print(df)
#Write to the CSV
#df.to_csv('GroupMakerOutput.csv')
#if client wants list to be completely randomized

'''
for i in range(len(result)):
    print("Group", i, ": ", end = "", sep = "")
    for j in range(1, len(result[i])):
        if (not j == len(result[i]) - 1):
            print(result[i][j], ", ", sep = "", end="")
        else:
            print(result[i][j])
'''

#print("new print") 
printOutput(result,randStudents,headers)           
            
timestamp = datetime.datetime.now().strftime("%m-%d-(%I-%M)")
outputFile = "GroupMakerOutput"+timestamp+".csv"

with open(outputFile, mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in result:
        csv_writer.writerow(row)
print("Successfully wrote to: ",outputFile)