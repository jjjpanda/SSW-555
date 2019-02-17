import sys
sys.dont_write_bytecode = True

import unittest
import datetime

def divorceBeforeDeath(family, husband, wife):
    """US06: Divorce can only occur before death of both spouses"""
    if family.divorce == "N/A" or husband.deathday == "N/A" or wife.deathday == "N/A": #if no divorce or one parent alive, then valid
        return True
    if husband.deathday <= family.divorce and wife.deathday <= family.divorce: #if both are dead before divorce, then invalid
        print(f"ERROR: (US06) Both spouses in family ({family.id}) died before a divorce occurred")
        return False
    return True


def yearDifference(date1, date2):
    """returns absolute value of difference between dates in years"""
    return abs(date2.year - date1.year - ((date2.month, date2.day) < (date1.month, date1.day)))

def marriageAfterAge(family, husband, wife):
    """Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
    if yearDifference(husband.birthday, family.marriage) < 14: #if husband is < 14, then invalid
        print(f"ERROR: (US10) Husband ({husband.id}: {husband.name}) in family ({family.id}) was younger than 14 years old ({yearDifference(family.marriage, husband.birthday)}) when he got married")
        return False
    if yearDifference(family.marriage, wife.birthday) < 14: #if wife is < 14, then invalid
        print(f"ERROR: (US10) Wife ({wife.id}: {wife.name}) in family ({family.id}) was younger than 14 years old ({yearDifference(family.marriage, wife.birthday)}) when she got married")
        return False
    return True

def main(individuals, families):
    for fam in families.values():
        divorceBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
        marriageAfterAge(fam, individuals[fam.husband], individuals[fam.wife])
