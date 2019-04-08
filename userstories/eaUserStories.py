#Evan Abel
import sys
sys.dont_write_bytecode = True
import unittest
from datetime import datetime, timedelta

#US02
def birthBeforeMarriage(individual, family):
    if family.marriage == "N/A":
        return True

    if individual.birthday > family.marriage or individual.birthday == family.marriage:
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

#US11 Marriage should not occur during marriage to another spouse
def noBigamy(family1, family2):
    if(family1=="N/A" or family2=="N/A"):
        return True

    if(family1.marriage < family2.marriage):
        if(family1.divorce == "N/A"):
            print("ERROR: FAMILY: US11: No divorce ever occurred")
            return False
        elif(family1.divorce < family2.marriage):
            return True
        else:
            print("ERROR: FAMILY: US11: Divorce occurred after second marriage")
            return False
    
    if(family2.marriage < family1.marriage):
        if(family2.divorce == "N/A"):
            print("ERROR: FAMILY: US11: No divorce ever occurred")
            return False
        elif(family2.divorce < family1.marriage):
            return True
        else:
            print("ERROR: FAMILY: US11: Divorce occurred after second marriage")
            return False

#US12 Mom less than 60 years older, dad less than 80 years older
def parentsNotTooOld(individual, dad, mom):
    momBirth = mom.birthday + timedelta(days=365.25*60)
    dadBirth = dad.birthday + timedelta(days=365.25*80)

    if(momBirth < individual.birthday or dadBirth < individual.birthday):
        print(f"ERROR: FAMILY: US12: Individual ({individual.id}) parent(s) is/are too old to give birth")
        return False
    else:
        return True

#US38 List all living people in a GEDCOM file whose birthdays occur in the next 30 days
def listUpcomingBirthdays(individual):
    thirtyDays = datetime.today() + timedelta(days=30)
    today = datetime.today()
    if (thirtyDays.month == today.month):
        if (thirtyDays.month == individual.birthday.month):
            if (today.day <= individual.birthday.day and thirtyDays.day >= individual.birthday.day):
                return True
            else:
                print("ERROR: Indivdiual's birthday is not in the next 30 days")
                return False
        else:
            print("ERROR: Indivdiual's birthday is not in the next 30 days")
            return False
    else:
        if (today.month == individual.birthday.month):
            if (individual.birthday.day >= today.month):
                return True
            else:
                print("ERROR: Indivdiual's birthday is not in the next 30 days")
                return False
        elif (thirtyDays.month == individual.birthday.month):
            if (individual.birthday.day <= thirtyDays.day):
                return True
            else:
                print("ERROR: Indivdiual's birthday is not in the next 30 days")
                return False
        else:
            print("ERROR: Indivdiual's birthday is not in the next 30 days")
            return False

#US39 List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
def listUpcomingAnniversaries(family):
    thirtyDays = datetime.today() + timedelta(days=30)
    today = datetime.today()
    if (thirtyDays.month == today.month):
        if (thirtyDays.month == family.marriage.month):
            if (today.day <= family.marriage.day and thirtyDays.day >= family.marriage.day):
                return True
            else:
                print("ERROR: Family's anniversary is not in the next 30 days")
                return False
        else:
            print("ERROR: Family's anniversary is not in the next 30 days")
            return False
    else:
        if (today.month == family.marriage.month):
            if (family.marriage.day >= today.month):
                return True
            else:
                print("ERROR: Family's anniversary is not in the next 30 days")
                return False
        elif (thirtyDays.month == family.marriage.month):
            if (family.marriage.day <= thirtyDays.day):
                return True
            else:
                print("ERROR: Family's anniversary is not in the next 30 days")
                return False
        else:
            print("ERROR: Family's anniversary is not in the next 30 days")
            return False

def main(individuals, families):
    for person in individuals.values():
        if (person.fams != "N/A"):
            birthBeforeMarriage(person, families[person.fams])
        birthBeforeDeath(person)