import sys
sys.dont_write_bytecode = True

import unittest
from datetime import datetime, timedelta

def IDatesInFuture(individuals):
    """ US01: No Date in individuals can happen after current date.
        Tests that any given individual has only valid dates.
                True: Date is valid
                False: Date is invalid because is in the future
    """
    for date in [individuals.birthday, individuals.deathday]:
        if date != "N/A":
            if date < datetime.today():
                return True
            else:
                print("ERROR: INDIVIDUAL: US01: individual with ID", individuals.id, "contains date", date.date(), "which occurs in the future")
                return False

def FDatesInFuture(families):
    """ US01: No Date in a family can happen after current date
        Tests that any given family has only valid dates.
                True: Date is valid
                False: Date is invalid because is in the future
    """
    for date in [families.marriage, families.divorce]:
        if date != "N/A":
            if date < datetime.today():
                return True
            else:
                print("ERROR: FAMILY: US01: family with ID", families.id, "contains date", date.date(), "which occurs in the future")
                return False

def ageGreaterThan(individual):
    """ US07: No individual can live more than 150 years.
            False: Individual lives more than 150 years.
    """
    if (individual.deathday == "N/A"):
        currentDate = datetime.now()
        age = currentDate.year - individual.birthday.year - ((currentDate.month, currentDate.day) < (individual.birthday.month, individual.birthday.day))
    else:
        age = individual.deathday.year - individual.birthday.year - ((individual.deathday.month, individual.deathday.day) < (individual.birthday.month, individual.birthday.day))
    if age < 150:
        return True
    else:
        print("ERROR: INDIVIDUAL: US07", individual.name, "with ID", individual.id, "lives more than 150 years. Birth date is", individual.birthday.date()) 
        return False

def birthBeforeMarriage(individual, family):
    """ US08: Children should be born after marriage of parents 
    and not more than 9 months after their divorce"""
    if individual.birthday < family.marriage and individual.famc != "N/A":
        print("ERROR: INDIVIDUAL: US08", individual.name, "with ID", individual.id, "is born before his/her parents got married")
        return False
    if family.divorce != "N/A":
        if individual.birthday > (family.divorce + timedelta(days=30*9)):
            print("ERROR: INDIVIDUAL: US08", individual.name, "with ID", individual.id, "is born over 9 months after his parents divorce")
            return False
    else:
        return True

def birthBeforeDeath(individual, mom, dad):
    """ US09: Child should be born before death of mother 
    and before 9 months after death of father """
    if mom.deathday != "N/A" and individual.birthday > mom.deathday:
        print("ERROR: INDIVIDUAL: US09", individual.name, "with ID", individual.id, "is born after his/her mom died")
        return False
    if dad.deathday != "N/A" and individual.birthday > (dad.deathday + timedelta(days=9*30)):
        print("ERROR: INDIVIDUAL: US09", individual.name, "with ID", individual.id, "is born over 9 months after his/her dad died")
        return False
    else:
        return True






def main(individuals, families):
    
    for fam in families.values():
        FDatesInFuture(fam)
    
    for individual in individuals.values():
        ageGreaterThan(individual)
        IDatesInFuture(individual)
        if individual.famc != "N/A":
            birthBeforeMarriage(individual, families[individual.famc])
            birthBeforeDeath(individual, individuals[families[individual.famc].wife], individuals[families[individual.famc].husband])