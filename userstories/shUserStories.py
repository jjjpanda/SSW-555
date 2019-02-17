import sys
sys.dont_write_bytecode = True

import unittest
from datetime import datetime

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

def main(individuals, families):
    for indi in individuals.values():
        ageGreaterThan(indi)
        IDatesInFuture(indi)
    for fam in families.values():
        FDatesInFuture(fam)


    