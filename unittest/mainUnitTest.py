import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mainGedcomParser as parser
import unittest
class TestGedcom(unittest.TestCase):
    def test_US06(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("../gedcoms/hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        #mygedcom.ge nTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertFalse(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))
    
    def test_US10(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("../gedcoms/hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        #mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertFalse(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))