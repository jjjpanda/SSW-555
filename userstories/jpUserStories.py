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

def main(individuals, families):
    for fam in families.values():
        marriageBeforeDivorce(fam)
        marriageBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
