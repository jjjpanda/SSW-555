#Herb Zieger
from prettytable import PrettyTable

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
        self.birthday = input
    def setDeathday(self, input):
        self.deathday = input
    def setSex(self, input):
        self.sex = input
    def setFamc(self, input):
        self.famc = input
    def setFams(self, input):
        self.fams = input
    def getValues(self): #get values in a list
        return [self.id, self.name, self.birthday, self.deathday, self.sex, self.famc, self.fams]
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
        self.marriage = input
    def setDivorce(self, input):
        self.divorce = input
    def setHusband(self, input):
        self.husband = input
    def setWife(self, input):
        self.wife = input
    def setChildren(self, input): #adds children ids to list of children
        self.children.append(input)
    def getValues(self): #get values in a list
        return self.id, self.marriage, self.divorce, self.husband, self.wife, str(self.children)
    def __repr__(self): #to string method
        return self.id+" "+self.marriage+" "+self.divorce+" "+self.husband+" "+self.wife+" "+str(self.children)

def printValid(level, tag, args): #print the parsed line in the specified format matching: --> "0 NOTE dates after now \n <-- 0|NOTE|Y|dates after now"
    print(level+"|"+tag+"|"+args) #

def addNewInstance(dict, id, type): #create new individual or family with id
    if (type == "F"):
        dict[id] = Family(id)
    if (type == "I"):
        dict[id] = Individual(id)
def addToInstance(dict, id, tag, args): #add to individual or family with specific tags
    if (tag == "NAME"):
        dict[id].setName(args)
    elif (tag == "BIRT"):
        dict[id].setBirthday(args)
    elif (tag == "DEAT"):
        dict[id].setDeathday(args)
    elif (tag == "SEX"):
        dict[id].setSex(args)
    elif (tag == "FAMC"):
        dict[id].setFamc(args)
    elif (tag == "FAMS"):
        dict[id].setFams(args)
    elif (tag == "MARR"):
        dict[id].setMarriage(args)
    elif (tag == "DIV"):
        dict[id].setDivorce(args)
    elif (tag == "HUSB"):
        dict[id].setHusband(args)
    elif (tag == "WIFE"):
        dict[id].setWife(args)
    elif (tag == "CHIL"):
        dict[id].setChildren(args)

def genTables(peopleDict, familyDict): #create prettytables with individuals and families
    peopleTable = PrettyTable() #table for individuals
    peopleTable.field_names = ["ID", "Name", "Birth Date", "Death Date", "Sex", "Famc", "Fams"]
    for item, values in peopleDict.items():
        peopleTable.add_row(values.getValues())
    print(peopleTable)

    familyTable = PrettyTable() #table for families
    familyTable.field_names = ["ID", "Marriage Date", "Divorce Date", "Husband", "Wife", "Children"]
    for item, values in familyDict.items():
        familyTable.add_row(values.getValues())
    print(familyTable)

levelZero = ["NOTE", "HEAD", "TRLR"] #possible tags for level zero
levelZeroWeird = ["INDI", "FAM"] #exceptions to normal format
levelOne = ["NAME", "SEX", "FAMC", "FAMS", "HUSB", "WIFE", "CHIL", "BIRT", "DEAT", "MARR", "DIV"] #possible tags for level one
levelTwo = ["DATE"] #possbile tags for level two

individuals = {}
families = {}

f = open("testFamily.ged", "r") #open file
input = f.read().splitlines() #save file as list of individual lines
for line in input: #More compact, but not as readable:
    words = line.split() #split lines into lists
    if (words[0] is "0" and words[1] in levelZero):
        printValid(words[0], words[1], ' '.join(words[2:]))
    elif (len(words) is 3 and words[0] is "0" and words[2] in levelZeroWeird): #check for weird level 0
        printValid(words[0], words[2], words[1])
        if (words[2] == "INDI"):
            currentID = words[1]
            currentDict = individuals
            currentType = "I"
            addNewInstance(currentDict, currentID, currentType)
        elif (words[2] == "FAM"):
            currentID = words[1]
            currentDict = families
            currentType = "F"
            addNewInstance(currentDict, currentID, currentType)
    elif(words[0] is "1" and words[1] in levelOne): #uses id from previous indi or fam tag
        printValid(words[0], words[1], ' '.join(words[2:]))
        addToInstance(currentDict, currentID, words[1], ' '.join(words[2:]))
        currentTag = words[1]
    elif ((words[0] is "2" and words[1] in levelTwo)): #uses tag from previous line if date tag is found
        printValid(words[0], words[1], ' '.join(words[2:]))
        addToInstance(currentDict, currentID, currentTag, ' '.join(words[2:]))

"""for indiv, value in individuals.items():
    print(value)
print("")
for family, value in families.items():
    print(value)"""
genTables(individuals, families)
