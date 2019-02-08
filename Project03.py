import os
import unittest
"""
This python app reads a GEDCOM file and filters out lines that are not valid per the project requirements.
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


class Individual:
    """Defines an individual and all possible charactersitics of an individual:
    Unique individual ID, Name, Sex/Gender, Birth date, Death date, 
    Unique Family ID where the individual is a child, Unique Family ID where the individual is a spouse"""
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.gender = ""
        self.birth = ""
        self.death = ""
        self.child = ""
        self.spouse = ""

    def __str__(self):
        return str("ID: "+ self.id + "| Name:" + self.name + "| Sex: " + self.gender + "| Birth:" + self.birth+ "| Died:" + self.death + "| Children: " + self.child + "| Spouse:" + self.spouse)
        

def gedcom_categorizer(file_name, gedcom):
    validlines_file = os.path.realpath(file_name)
    try:
        fp = open(validlines_file, 'r') # Do the risky action of attempting to open a file
    except FileNotFoundError:
        print("can't open", file_name) # If file not found, raise exception
    else: # If the file is found
        with fp:

            current_id = None #initiate current_id variable that will be used when parser sees an instance initiator
            nexttagbirt = False # set a flag that identifies when the following date is for birth (true) or death (false)
            
            for line in fp:
                line = line.rstrip('\n\r').split("|") # split lines into a list

                if line[0] == "0" and line[1] == "INDI": # if we identify a new instance of individual, create instance
                    current_id = line[2]
                    gedcom.individual[current_id] = Individual(current_id)
                                
                if line[0] != "0": # if this is level 1 or 2, we are defining an already created instance of individual
                    # add args to instance of Individual
                    if line[1] == "SEX":
                        gedcom.individual[current_id].gender = line[2]
                    elif line[1] == "NAME":
                        gedcom.individual[current_id].name = line[2]
                    elif line[1] == "FAMC":
                        gedcom.individual[current_id].child = line[2]
                    elif line[1] == "FAMS":
                        gedcom.individual[current_id].spouse = line[2]
                    #if a birth or death is present, set value for flag so following date gets added to the right attribute
                    elif line[1] == "BIRT":
                        nexttagbirt = True
                    elif line[1] == "DEAT":
                        nexttagbirt = False
                    # set date to appropriate attribute
                    elif line[1] == "DATE":
                        if nexttagbirt:
                            gedcom.individual[current_id].birth = line[2]
                        else:
                            gedcom.individual[current_id].death = line[2]
                

def main():
    mygedcom = GedcomFile()
    
    gedcom_cleaner("Project01GEDCOM.txt")
    gedcom_categorizer("validlines.txt", mygedcom)

    for ID in mygedcom.individual:
        print(mygedcom.individual[ID])

if __name__ == '__main__':
    main()
    