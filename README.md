# GroupMaker
GroupMaker.py is a Python3-based program that will create groups based on a CSV file. The product will import the CSV file, parse through it, and ultimately group students together based on the condition that the user chooses. <br/><br/>The user will be able to sort groups based on blacklists and other custom metrics. The user will also be able to set the number of groups once they start running the program. The program will display the groups to the user after they are created. It will also create an output CSV that will contain all the groups that have been run by the program.

## Dependencies
<ul>
  <li>Python 3</li>
  <li>Pandas</li>
  <li>Numpy</li>
</ul>

## How to Install and Run the Program
```bash
# Install dependencies

# Install Python 3
$ sudo apt-get install python3

# Install Pandas
$ sudo apt-get install python3-pandas

# Install Numpy
$ sudo apt-get install python3-numpy

#Running the Program 
$ python3 GroupMaker.py
```
## How to use
Enter the input CSV when prompted and answer the questions as they appear to create your groups<br/>
** Make sure that the input CSV is in the same directory as the program**<br/>
The output CSV is stored in the same folder as the program 

## Input CSV Details
The input CSV must be in the following format. The first two columns must be labled "Name" and "Blacklist" in that order. <br/>The last three columns are custom categories and can be labled as anything the user wishes. <br/>
If the student does not have a student to blacklist you can leave the field blank. 
## Example CSV Format

| Name    | Blacklist| Custom Category 1 (Favorite Console)  | Custom Category 2 (Favorite Color)|Custom Category 3 (Favorite Sport) |
|:-------:|:--------:|:------:|:-----:|:-----:|
| Jose    | Daniel   | Xbox   | Red   |   Soccer   |
| Daniel  |          | Wii    | Blue    |  Basketball    |
|Steve    |   Mary   | PS4    |  Blue    |  Baseball    |
| Mary    |          | Wii    |  Green    |   Soccer   |


## Authors
<ul>
  <li>Anthony Phimmasone</li>
  <li>James Donahue</li>
  <li>Igor Asipenka</li>
  <li>Denzel Saraka</li>
</ul>

