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

def test(individuals, families):
    for fam in families.values():
        divorceBeforeDeath(fam, individuals[fam.husband], individuals[fam.wife])
        marriageAfterAge(fam, individuals[fam.husband], individuals[fam.wife])

'''class TestSprintOne(unittest.TestCase):
    def test_US06(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        #mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(divorceBeforeDeath(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertFalse(divorceBeforeDeath(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(divorceBeforeDeath(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(divorceBeforeDeath(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertTrue(divorceBeforeDeath(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))
    
    def test_US10(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        #mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(marriageAfterAge(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(marriageAfterAge(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(marriageAfterAge(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(marriageAfterAge(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertFalse(marriageAfterAge(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))
    '''