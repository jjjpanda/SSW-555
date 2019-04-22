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


def noIncest(familyID, husband, wife):
    """US18: Siblings should not marry one another"""
    if husband.parents != "N/A" and husband.parents == wife.parents:
        print(f"ERROR: FAMILY: US18: Marriage in family ({familyID}) is incestous.")
        return False
    return True
        

def correctGender(familyID, husband, wife):
    """US21: Husband in family should be male and wife in family should be female"""
    if husband.sex == "M" and wife.sex == "F":
        return True
    else:
        print(f"ERROR: FAMILY: US21: Marriage in family ({familyID}) has incorrect genders.")
        return False

def orderSiblings(listOfChildren, individuals):
    if len(listOfChildren) <= 1:
        return listOfChildren
    listOfAges = []
    for person in listOfChildren:
        listOfAges.append(individuals[person].getAge())
    return [listOfChildren for _,listOfChildren in sorted(zip(listOfAges,listOfChildren),reverse=True)]
    
def correspondingEntriesFromFamilies(fam, individuals):
    if individuals[fam.husband].fams != individuals[fam.wife].fams:    
        print(f"ERROR: US26: No corresponding entry for spouse in individuals for ({fam.id})")
        return False
    if len(fam.children) > 0:
        for child in fam.children:
            if fam.id != individuals[child].parents:
                print(f"ERROR: US26: No corresponding entry for children in individuals for ({fam.id})")
                return False
    return True


def correspondingEntriesFromIndividuals(individual, families):
    if individual.famc != "N/A" and individual.id not in families[individual.famc].children:
        print(f"ERROR: US26: No corresponding entry for child in families for ({individual.id})")
        return False
    if individual.fams != "N/A" and (individual.id not in families[individual.fams].husband or individual.id not in families[individual.fams].wife):
        print(f"ERROR: US26: No corresponding entry for spouse in families for ({individual.id})")
        return False
    return True

def main(individuals, families):
    for fam in families.values():
        marriageBeforeDivorce(fam)
        marriageBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
        noIncest(fam.id, individuals[fam.husband], individuals[fam.wife])
        correctGender(fam.id, individuals[fam.husband], individuals[fam.wife])
        correspondingEntriesFromFamilies(fam, individuals)
    #for individual in individuals.values:
        #correspondingEntriesFromIndividuals(individual, families)