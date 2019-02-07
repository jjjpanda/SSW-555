#Herb Zieger
def printValid(original, level, tag, args, isValid): #print the parsed line in the specified format matching: --> "0 NOTE dates after now \n <-- 0|NOTE|Y|dates after now"
    print("--> "+original+"\n<-- "+level+"|"+tag+"|"+isValid+"|"+args)
levelZero = ["NOTE", "HEAD", "TRLR"] #possible tags for level zero
levelZeroWeird = ["INDI", "FAM"] #exceptions to normal format
levelOne = ["NAME", "SEX", "FAMC", "FAMS", "HUSB", "WIFE", "CHIL", "BIRT", "DEAT", "MARR", "DIV"] #possible tags for level one
levelTwo = ["DATE"] #possbile tags for level two
f = open("testFamily.ged", "r") #open file
input = f.read().splitlines() #save file as list of individual lines
for line in input: #More compact, but not as readable:
    words = line.split() #split lines into lists
    if ((words[0] is "0" and words[1] in levelZero) or (words[0] is "1" and words[1] in levelOne) or (words[0] is "2" and words[1] in levelTwo)): # check for normal valid
        printValid(line, words[0], words[1], ' '.join(words[2:]), "Y")
    elif (words[0] is "0" and words[2] in levelZeroWeird): #check for weird level 0
        printValid(line, words[0], words[2], words[1], "Y")
    else: #if it dosen't fit the above condidtions, it is invalid
        printValid(line, words[0], words[1], ' '.join(words[2:]), "N")