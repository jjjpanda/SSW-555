import sys
sys.dont_write_bytecode = True

import datetime

def marriageBeforeDivorce(family):
    """US04: Marriage should occur before divorce of spouses, and divorce can only occur after marriage"""
    if family.divorce == "N/A" or family.divorce > family.marriage:
        return True
    if family.divorce != "N/A" or family.divorce < family.marriage:
        print(f"ERROR: FAMILY: US04: Marriage in family ({family.id}) occurrs after divorce.")
        return False

def marriageBeforeDeath(family, husband, wife):
    """US05: Marriage should occur before death of either spouse"""
    if not husband.isAlive() and family.marriage > husband.deathday:
        print(f"ERROR: FAMILY: US05: Marriage in family ({family.id}) occurrs after death of ({husband.name}) ID: ({husband.id}).")
        return False
    if not wife.isAlive() and family.marriage > wife.deathday:
        print(f"ERROR: FAMILY: US05: Marriage in family ({family.id}) occurrs after death of ({wife.name}) ID: ({wife.id}).")
        return False
    else:
        return True


def incest(family, husband, wife):
    """US18: Siblings should not marry one another"""

def correctGender(family, husband, wife):
    """US21: Husband in family should be male and wife in family should be female"""

def main(individuals, families):
    for fam in families.values():
        marriageBeforeDivorce(fam)
        marriageBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
        incest(fam, individuals[fam.husband], individuals[fam.wife])
        correctGender(fam, individuals[fam.husband], individuals[fam.wife])
