#Herb Zieger
from prettytable import PrettyTable

class Individual:
    def __init__(self, id):
        self.id = id
        self.name = "N/A"
        self.birthday = "N/A"
        self.deathday = "N/A"
        self.sex = "N/A"
        self.famc = "N/A"
        self.fams = "N/A"
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
    def getValues(self):
        return [self.id, self.name, self.birthday, self.deathday, self.sex, self.famc, self.fams]
    def __repr__(self):
        return self.id+" "+self.name+" "+self.birthday+" "+self.deathday+" "+self.sex+" "+self.famc+" "+self.fams

class Family:
    def __init__(self, id):
        self.id = id
        self.marriage = "N/A"
        self.divorce = "N/A"
        self.husband = "N/A"
        self.wife = "N/A"
        self.children = []
    def setMarriage(self, input):
        self.marriage = input
    def setDivorce(self, input):
        self.divorce = input
    def setHusband(self, input):
        self.husband = input
    def setWife(self, input):
        self.wife = input
    def setChildren(self, input):
        self.children.append(input)
    def getValues(self):
        return self.id, self.marriage, self.divorce, self.husband, self.wife, str(self.children)
    def __repr__(self):
        return self.id+" "+self.marriage+" "+self.divorce+" "+self.husband+" "+self.wife+" "+str(self.children)

def printValid(original, level, tag, args, isValid): #print the parsed line in the specified format matching: --> "0 NOTE dates after now \n <-- 0|NOTE|Y|dates after now"
    print(level+"|"+tag+"|"+args)

def addNewInstance(dict, id, type):
    if (type == "F"):
        dict[id] = Family(id)
    if (type == "I"):
        dict[id] = Individual(id)
def addToInstance(dict, id, tag, args):
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

def genTables(peopleDict, familyDict):
    peopleTable = PrettyTable()
    peopleTable.field_names = ["ID", "Name", "Birth Date", "Death Date", "Sex", "Famc", "Fams"]
    for item, values in peopleDict.items():
        peopleTable.add_row(values.getValues())
    print(peopleTable)

    familyTable = PrettyTable()
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
currentID = ""


f = open("testFamily.ged", "r") #open file
input = f.read().splitlines() #save file as list of individual lines
for line in input: #More compact, but not as readable:
    words = line.split() #split lines into lists
    if (words[0] is "0" and words[1] in levelZero):
        printValid(line, words[0], words[1], ' '.join(words[2:]), "Y")
    elif (len(words) is 3 and words[0] is "0" and words[2] in levelZeroWeird): #check for weird level 0
        printValid(line, words[0], words[2], words[1], "Y")
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
    elif(words[0] is "1" and words[1] in levelOne):
        printValid(line, words[0], words[1], ' '.join(words[2:]), "Y")
        addToInstance(currentDict, currentID, words[1], ' '.join(words[2:]))
        currentTag = words[1]
    elif ((words[0] is "2" and words[1] in levelTwo)): # check for normal valid
        printValid(line, words[0], words[1], ' '.join(words[2:]), "Y")
        addToInstance(currentDict, currentID, currentTag, ' '.join(words[2:]))
    #else: #if it dosen't fit the above condidtions, it is invalid
       # printValid(line, words[0], words[1], ' '.join(words[2:]), "N")

"""for indiv, value in individuals.items():
    print(value)
print("")
for family, value in families.items():
    print(value)"""
genTables(individuals, families)
