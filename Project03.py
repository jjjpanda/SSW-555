import os
import unittest
from prettytable import PrettyTable
from datetime import datetime

"""
This python app reads a GEDCOM file and filters out lines that are not valid per the project requirements.
Then it extracts individuals and families out of the new clean text file.
"""

def gedcom_cleaner(file_name):
    """        
    The steps followed to clean the GEDCOM file are:
    1. read GEDCOM file, and make each line a list of strings
    2. as per standard GEDCOM formatting, set level, tag, and args to their positions.
    3. if the INDI or FAM tags are present, the tag and args switch positions
    4. with elements of the line labeled, check against a dictionary of gedcom_rules to ensure all valid combinations.
    5. once categorized between valid and invalid, print only valid lines.
    """
        
    gedcom_rules = {'0': {'INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'},
                    '1': {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'},
                    '2': {'DATE'}}
    
    open("validlines.txt", "w").close()
    gedcom_file = os.path.realpath(file_name)
    try:
        fp = open(gedcom_file, 'r') # Do the risky action of attempting to open a file
    except FileNotFoundError:
        print("can't open", file_name) # If file not found, raise exception
    else: # If the file is found
        with fp:
            
            for line in fp:
                input_line = line.rstrip('\n\r') #Strips the \n and/or \r from the end of the line, and preserve original line
                line = input_line.split(" ", 2) # Separates the line into values using the separator
                
                level = line[0] #set the 'level'
                tag = line[1] #set the 'tag' to be second position as it is in standard case
                if len(line) > 2: #if there is a third element, make it 'args' aas in standard case
                    args = line[2]
                    #if we have 'INDI' or 'FAM', the args and tag are in opposite positions
                    if line[0] == '0' and line[2] in ('INDI', 'FAM'):
                        tag, args = args, tag
                else:
                    args = ""

                # With variables set, check that their combinations are valid
                if (level in gedcom_rules.keys()) and (tag in gedcom_rules[level]) and (line[1] != 'FAM') and (line[1] != 'INDI'): #also check that 'FAM' and 'INDI' are not on the second position
                    outFile = open("validlines.txt", "a")
                    outFile.write(f"{level}|{tag}|{args}\n")
                else: #if combination of characters is not allowed in that order, pring with a 'N' flag
                    continue
              

class GedcomFile:
    """ Class GedcomFile imports all individual and family 
    data from a Gedcom file and organizes them into dictionaries""" 

    def __init__(self):
        self.individual = dict() #an instance of individual will be saved on self.individual[id]
        self.family = dict() #an instance of family will be saved in self.family[id]

    def genTables(self, peopleDict, familyDict): #create prettytables with individuals and families
        peopleTable = PrettyTable() #table for individuals
        peopleTable.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death Date", "Child", "Spouse"]
        for item, values in sorted(peopleDict.items()):
            peopleTable.add_row([values.id, values.name, values.sex, datetoString(values.birthday), values.getAge(), values.isAlive(), datetoString(values.deathday), values.famc, values.fams])
        print(peopleTable)

        familyTable = PrettyTable() #table for families
        familyTable.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
        for item, values in sorted(familyDict.items()):
            familyTable.add_row([values.id, datetoString(values.marriage), datetoString(values.divorce), values.husband, peopleDict[values.husband].name, values.wife, peopleDict[values.wife].name, str(values.children)])
        print(familyTable)


class Individual: #class for individuals
    def __init__(self, id): #constructor only set id at creation
        self.id = id
        self.name = "N/A"
        self.birthday = "N/A"
        self.deathday = "N/A"
        self.sex = "N/A"
        self.famc = "N/A"
        self.fams = "N/A"
    #setter methods to change values
    def setName(self, input):
        self.name = input
    def setBirthday(self, input):
        self.birthday = stringToDate(input)
    def setDeathday(self, input):
        self.deathday = stringToDate(input)
    def setSex(self, input):
        self.sex = input
    def setFamc(self, input):
        self.famc = input
    def setFams(self, input):
        self.fams = input
    def isAlive(self):
        return True if self.deathday == "N/A" else False
    def getAge(self):
        if (self.deathday == "N/A"):
            currentDate = datetime.now()
            return currentDate.year - self.birthday.year - ((currentDate.month, currentDate.day) < (self.birthday.month, self.birthday.day))
        else:
            return self.deathday.year - self.birthday.year - ((self.deathday.month, self.deathday.day) < (self.birthday.month, self.birthday.day))
    def __repr__(self): #to string method
        return self.id+" "+self.name+" "+self.birthday+" "+self.deathday+" "+self.sex+" "+self.famc+" "+self.fams

class Family: #constructor only set id at creation
    def __init__(self, id):
        self.id = id
        self.marriage = "N/A"
        self.divorce = "N/A"
        self.husband = "N/A"
        self.wife = "N/A"
        self.children = []
    #setter methods to change values
    def setMarriage(self, input):
        self.marriage = stringToDate(input)
    def setDivorce(self, input):
        self.divorce = stringToDate(input)
    def setHusband(self, input):
        self.husband = input
    def setWife(self, input):
        self.wife = input
    def setChildren(self, input): #adds children ids to list of children
        self.children.append(input)
    def __repr__(self): #to string method
        return self.id+" "+self.marriage+" "+self.divorce+" "+self.husband+" "+self.wife+" "+str(self.children)

def stringToDate(strInput):
    try:
        return datetime.strptime(strInput, "%d %b %Y")
    except:
        return strInput

def datetoString(dateInput):
    try:
        return datetime.strftime(dateInput, "%Y-%m-%d")
    except:
        return dateInput



def gedcom_categorizer(file_name, gedcom):
    validlines_file = os.path.realpath(file_name)
    try:
        fp = open(validlines_file, 'r') # Do the risky action of attempting to open a file
    except FileNotFoundError:
        print("can't open", file_name) # If file not found, raise exception
    else: # If the file is found
        with fp:

            current_id = None #initiate current_id variable that will be used when parser sees an instance initiator
            nextbirth = False # set a flag that identifies when the following date is for birth (true) or death (false)
            nextdeath = False
            nextmarriage = False
            nextdivorce = False
            
            for line in fp:
                line = line.rstrip('\n\r').split("|") # split lines into a list

                if line[0] == "0" and line[1] == "INDI": # if we identify a new instance of individual, create instance
                    current_id = line[2]
                    gedcom.individual[current_id] = Individual(current_id)
                
                if line[0] == "0" and line[1] == "FAM":
                    current_id = line[2]
                    gedcom.family[current_id] = Family(current_id) # if we identify a new instance of family, create instance
                       
                if line[0] != "0": # if this is level 1 or 2, we are defining an already created instance of individual or family
                    # add args to instance of Individual or family
                    if line[1] == "SEX":
                        gedcom.individual[current_id].setSex(line[2])
                    elif line[1] == "NAME":
                        gedcom.individual[current_id].setName(line[2])
                    elif line[1] == "FAMC":
                        gedcom.individual[current_id].setFamc(line[2])
                    elif line[1] == "FAMS":
                        gedcom.individual[current_id].setFams(line[2])
                    elif line[1] == "HUSB":
                        gedcom.family[current_id].setHusband(line[2])
                    elif line[1] == "WIFE":
                        gedcom.family[current_id].setWife(line[2])
                    elif line[1] == "CHIL":
                        gedcom.family[current_id].setChildren(line[2])
                    # if any of the following four are present, set the flag so DATE can be assigned to proper tag
                    elif line[1] == "BIRT":
                        nextbirth = True
                    elif line[1] == "DEAT":
                        nextdeath = True
                    elif line[1] == "MARR":
                        nextmarriage = True
                    elif line[1] == "DIV":
                        nextdivorce == True
                    
                    # set date to appropriate attribute
                    elif line[1] == "DATE":
                        if nextbirth:
                            gedcom.individual[current_id].setBirthday(line[2])
                            nextbirth = False
                        elif nextdeath:
                            gedcom.individual[current_id].setDeathday(line[2])
                            nextdeath = False
                        elif nextmarriage:
                            gedcom.family[current_id].setMarriage(line[2])
                            nextmarriage = False
                        elif nextdivorce:
                            gedcom.family[current_id].setDivorce(line[2])
                            nextdivorce = False

                
                    

def main():
    mygedcom = GedcomFile()
    
    gedcom_cleaner("testFamily.ged")
    gedcom_categorizer("validlines.txt", mygedcom)

    mygedcom.genTables(mygedcom.individual, mygedcom.family)
    
    
if __name__ == '__main__':
    main()
    