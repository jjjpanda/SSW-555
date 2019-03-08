#Evan Abel
import sys
sys.dont_write_bytecode = True
import unittest
from datetime import datetime, timedelta

#US02
def birthBeforeMarriage(individual, family):
    if family.marriage == "N/A":
        return True

    if individual.birthday > family.marriage:
        print(f"ERROR: INDIVIDUAL: US02: Individual ({individual.id}) was married before they were born")
        return False
    else:
        return True

#US03
def birthBeforeDeath(individual):
    if individual.deathday == "N/A":
        return True

    if individual.birthday > individual.deathday:
        print(f"ERROR: INDIVIDUAL: US03: Individual ({individual.id}) died before they were born")
        return False
    else:
        return True

#US12 Mom less than 60 years older, dad less than 80 years older
def parentsNotTooOld(individual, dad, mom):
    momBirth = mom.birthday + timedelta(days=365*60)
    dadBirth = dad.birthday + timedelta(days=365*80)

    if(momBirth < individual.birthday or dadBirth < individual.birthday):
        print(f"ERROR: FAMILY: US12: Individual ({individual.id}) parent(s) is/are too old to give birth")
        return False

    if(momBirth > individual.birthday and dadBirth > individual.birthday):
        return True

def noBigamy(family1, family2):
    if(family1.marriage < family2.marriage):
        if(family1.divorce == "N/A"):
            return False
        else:
            return True
    elif(family2.marriage < family1.marriage):
        if(family2.divorce == "N/A"):
            return False
        else:
            return True


    


def main(individuals, families):
    for person in individuals.values():
        if (person.fams != "N/A"):
            birthBeforeMarriage(person, families[person.fams])
        birthBeforeDeath(person)