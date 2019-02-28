import sys
sys.dont_write_bytecode = True

import unittest
import datetime

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

def marriageAfterAge(family, husband, wife):
    """US10: Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
    if yearDifference(husband.birthday, family.marriage) < 14: #if husband is < 14, then invalid
        print(f"ERROR: FAMILY: US10: Husband ({husband.id}: {husband.name}) in family ({family.id}) was younger than 14 years old ({yearDifference(family.marriage, husband.birthday)}) when he got married")
        return False
    if yearDifference(family.marriage, wife.birthday) < 14: #if wife is < 14, then invalid
        print(f"ERROR: FAMILY: US10: Wife ({wife.id}: {wife.name}) in family ({family.id}) was younger than 14 years old ({yearDifference(family.marriage, wife.birthday)}) when she got married")
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


def main(individuals, families):
    for fam in families.values():
        divorceBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
        marriageAfterAge(fam, individuals[fam.husband], individuals[fam.wife])
        noMoreThanQuintuplets(fam, individuals)
        fewerThanFifteenSiblings(fam)
