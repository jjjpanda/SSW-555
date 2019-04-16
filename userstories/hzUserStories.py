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

def divorceBeforeDeath(family, husband, wife):
    """US06: Divorce can only occur before death of both spouses"""
    if family.divorce == "N/A" or husband.deathday == "N/A" or wife.deathday == "N/A": #if no divorce or one parent alive, then valid
        return True
    if husband.deathday <= family.divorce and wife.deathday <= family.divorce: #if both are dead before divorce, then invalid
        print(f"ERROR: FAMILY: US06: Both spouses in family ({family.id}) died before a divorce occurred")
        return False
    return True

def yearDifference(date1, date2):
    """returns absolute value of difference between dates in years"""
    return abs(date2.year - date1.year - ((date2.month, date2.day) < (date1.month, date1.day)))

def marriageAfterFourteen(family, husband, wife):
    """US10: Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
    husbandAgeAtMarriage = yearDifference(family.marriage, husband.birthday)
    wifeAgeAtMarriage = yearDifference(family.marriage, wife.birthday)
    if husbandAgeAtMarriage < 14: #if husband is < 14, then invalid
        print(f"ERROR: FAMILY: US10: Husband ({husband.id}: {husband.name}) in family ({family.id}) was younger than 14 years old ({husbandAgeAtMarriage}) when he got married")
        return False
    if wifeAgeAtMarriage < 14: #if wife is < 14, then invalid
        print(f"ERROR: FAMILY: US10: Wife ({wife.id}: {wife.name}) in family ({family.id}) was younger than 14 years old ({wifeAgeAtMarriage}) when she got married")
        return False
    return True

def noMoreThanQuintuplets(family, individuals):
    """US14: No more than five siblings should be born at the same time"""
    birthdays = []
    for sibling in family.children:
        birthdays.append(individuals[sibling].birthday)
    for birthday in birthdays:
        if birthdays.count(birthday) > 5:
            print(f"ERROR: FAMILY: US14: Family ({family.id}) has > 5 siblings ({birthdays.count(birthday)}) with the same birthday ({birthday.strftime('%Y-%m-%d')})")
            return False
    return True

def fewerThanFifteenSiblings(family):
    """US15: There should be fewer than 15 siblings in a family"""
    if len(family.children) < 15:
        return True
    else:
        print(f"ERROR: FAMILY: US15: Family ({family.id}) has > 15 siblings ({len(family.children)})")
        return False

def listRecentBirths(individuals):
    """US35: List all people in a GEDCOM file who were born in the last 30 days"""
    recentBirths = []
    for individual in individuals:
        if(isinstance(individual.birthday, datetime) and dates_within(individual.birthday, datetime.today(), 30, 'days')):
            recentBirths.append(individual.id)
    print(f"US35: These are the individuals who were born in the last 30 days:\n{recentBirths}") if (len(recentBirths) > 0) else ""
    return recentBirths

def listRecentDeaths(individuals):
    """US36: List all people in a GEDCOM file who died in the last 30 days"""
    recentDeaths = []
    for individual in individuals:
        if(isinstance(individual.deathday, datetime) and dates_within(individual.deathday, datetime.today(), 30, 'days')):
            recentDeaths.append(individual.id)
    print(f"US36: These are the individuals who died in the last 30 days:\n{recentDeaths}") if (len(recentDeaths) > 0) else ""
    return recentDeaths
def listLargeAgeDifference(individuals, families):
    """US34: List all couples who were married when the older spouse was more than twice as old as the younger spouse"""
    largeAgeDifferences = []
    for family in families:
        diff = abs(individuals[family.husband].getAge() - individuals[family.wife].getAge())
        if (diff > 2*individuals[family.husband].getAge() or diff > 2*individuals[family.wife].getAge()):
            largeAgeDifferences.append(family.id)
    print(f"US34: These are the families whose spouses have a large age difference:\n{largeAgeDifferences}") if (len(largeAgeDifferences) > 0) else ""
    return largeAgeDifferences
def main(individuals, families):
    listRecentBirths(individuals.values())
    listRecentDeaths(individuals.values())
    listLargeAgeDifference(individuals, families.values())
    for fam in families.values():
        divorceBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
        marriageAfterFourteen(fam, individuals[fam.husband], individuals[fam.wife])
        noMoreThanQuintuplets(fam, individuals)
        fewerThanFifteenSiblings(fam)
