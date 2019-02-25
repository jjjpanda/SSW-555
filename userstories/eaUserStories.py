#Evan Abel
import sys
sys.dont_write_bytecode = True
import unittest
import datetime

def birthBeforeMarriage(individual, family):
    if family.marriage == "N/A":
        return True

    if individual.birthday > family.marriage:
        print(f"ERROR: (US02) Individual ({individual.id}) was married before they were born")
        return False
    else:
        return True

def birthBeforeDeath(individual):
    if individual.deathday == "N/A":
        return True

    if individual.birthday > individual.deathday:
        print(f"ERROR: (US03) Individual ({individual.id}) died before they were born")
        return False
    else:
        return True

def main(individuals, families):
    for person in individuals.values():
        if (person.fams != "N/A"):
            birthBeforeMarriage(person, families[person.fams])
        birthBeforeDeath(person)