import sys
sys.dont_write_bytecode = True

import unittest
from datetime import datetime, timedelta

def dates_within(dt1, dt2, limit, units):
    """ Helper function to several others.
        returns True if dt1 and dt2 are within limit units, where 
        dt1, dt2 are instances of datetime
        limit is a number
        units is a string in ('days', 'months', 'years')
    """
    units = units.lower()
    conversion = {'days':1, 'months':30.4, 'years':365.25}
    return ((abs((dt1 - dt2).days) / conversion[units]) < limit) if units in ('days', 'months', 'years') else None
    

def IDatesInFuture(individuals):
    """ US01: No Date in individuals can happen after current date.
        Tests that any given individual has only valid dates.
                True: Date is valid
                False: Date is invalid because is in the future
    """
    for date in [individuals.birthday, individuals.deathday]:
        if date != "N/A" and date < datetime.today():
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
        if date != "N/A" and date < datetime.today():
            return True
        else:
            print("ERROR: FAMILY: US01: family with ID", families.id, "contains date", date.date(), "which occurs in the future")
            return False

def ageGreaterThan(individual):
    """ US07: No individual can live more than 150 years.
            False: Individual lives more than 150 years.
    """
    dt2 = individual.deathday if individual.deathday != 'N/A' else datetime.today()
    if dates_within(individual.birthday, dt2, 150, 'years'):
            return True
    else:
            print("ERROR: INDIVIDUAL: US07", individual.name, "with ID", individual.id, "lives more than 150 years. Birth date is", individual.birthday.date()) 
            return False

def birthBeforeMarriage(individual, family):
    """ US08: Children should be born after marriage of parents 
    and not more than 9 months after their divorce
    """
    if individual.birthday < family.marriage and individual.famc != "N/A":
        print("ERROR: INDIVIDUAL: US08", individual.name, "with ID", individual.id, "is born before his/her parents got married")
        return False
    if family.divorce != "N/A" and individual.birthday > (family.divorce + timedelta(days=30*9)):
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

def checkLivingMarried(individual):
    """ US30: Helper function for US30. Checks if individual meets conditions of being alive and married"""
    return True if individual.fams != 'N/A' and individual.deathday == 'N/A' else False

def list_LivingMarried(individuals):
    """ US30: Uses checkLivingMarried to decide which individuals to add to the LivingMarried list """
    livingMarried = [individual.id for individual in individuals.values() if checkLivingMarried(individual) == True]
    print("These are the individuals who are Married and still alive:")
    print(livingMarried)
    return(livingMarried)

def checkLivingSingle(individual):
    """ US31: Helper function for US31. Checks if individual meets conditions of being alive, older than 30 and never been married"""
    return True if individual.fams == 'N/A' and individual.deathday == 'N/A' and not(dates_within(individual.birthday, datetime.today(), 30, 'years')) else False

def list_LivingSingle(individuals):
    """ US31: Uses checkLivingSingle to decide which individuals to add to the LivingSingle list """
    livingSingle = [individual.id for individual in individuals.values() if checkLivingSingle(individual) == True]
    print("These are the individuals who are Single, alive, and over 30 years old:")
    print(livingSingle)
    return(livingSingle)


def main(individuals, families):

    # for indi, fam in individuals.values(), families.values():
    #     IDatesInFuture(indi, fam)

    list_LivingMarried(individuals)

    for family in families.values():
        FDatesInFuture(family)
   
    for individual in individuals.values():
        ageGreaterThan(individual)
        IDatesInFuture(individual)
        if individual.famc != "N/A":
            birthBeforeMarriage(individual, families[individual.famc])
            birthBeforeDeath(individual, individuals[families[individual.famc].wife], individuals[families[individual.famc].husband])
        
    