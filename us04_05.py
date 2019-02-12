from collections import Counter

def marriageBeforeDivorce(dateOfMarriage, dateOfDivorce):
    if (dateOfDivorce == "" or dateOfMarriage < dateOfDivorce):
        return True

    else :
          return False

def marriageBeforeDeath(dateOfMarriage, husband, wife):
    if (dateOfMarriage > husband.deathday and dateOfMarriage > wife.deathday):
        return True

    else:
         return False