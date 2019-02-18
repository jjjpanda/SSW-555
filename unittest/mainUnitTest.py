import sys
sys.dont_write_bytecode = True
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mainGedcomParser as parser
import unittest

#python ./unittest/mainUnitTest.py TestGedcom.test_US##

class TestGedcom(unittest.TestCase):
    def test_US01(self):
        """ Tests US01: No Date can happen after current date. 
        Tests that any given individual / family has only valid dates.
                True: Date is valid
                False: Date is invalid because is in the future
        """
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/shSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)

        self.assertFalse(parser.shUserStories.IDatesInFuture(mygedcom.individual["@I2@"]))
        self.assertTrue(parser.shUserStories.IDatesInFuture(mygedcom.individual["@I1@"]))
        self.assertTrue(parser.shUserStories.IDatesInFuture(mygedcom.individual["@I3@"]))
        self.assertTrue(parser.shUserStories.IDatesInFuture(mygedcom.individual["@I4@"]))
        self.assertTrue(parser.shUserStories.IDatesInFuture(mygedcom.individual["@I5@"]))
        self.assertFalse(parser.shUserStories.IDatesInFuture(mygedcom.individual["@I6@"]))

        self.assertTrue(parser.shUserStories.FDatesInFuture(mygedcom.family["@F2@"]))
        self.assertTrue(parser.shUserStories.FDatesInFuture(mygedcom.family["@F1@"]))
        self.assertFalse(parser.shUserStories.FDatesInFuture(mygedcom.family["@F3@"]))
        self.assertIsInstance(mygedcom.family["@F1@"], parser.Family)
        self.assertNotIsInstance(mygedcom.family["@F1@"], parser.Individual)
   
    def test_US04(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/jpSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.jpUserStories.marriageBeforeDivorce(mygedcom.family["@F1@"]))
        self.assertFalse(parser.jpUserStories.marriageBeforeDivorce(mygedcom.family["@F2@"]))
        self.assertTrue(parser.jpUserStories.marriageBeforeDivorce(mygedcom.family["@F3@"]))
        self.assertTrue(parser.jpUserStories.marriageBeforeDivorce(mygedcom.family["@F4@"]))
        self.assertTrue(parser.jpUserStories.marriageBeforeDivorce(mygedcom.family["@F5@"]))
        
    def test_US05(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/jpSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.jpUserStories.marriageBeforeDeath(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(parser.jpUserStories.marriageBeforeDeath(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.jpUserStories.marriageBeforeDeath(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.jpUserStories.marriageBeforeDeath(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertTrue(parser.jpUserStories.marriageBeforeDeath(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))

    def test_US06(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        #mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertFalse(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))

    def test_US07(self):
        """ Tests US01: No Date can happen after current date. 
        Tests that any given individual has only valid dates.
                True: Date is valid
                False: Date is invalid because is in the future
        """
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/shSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)

        self.assertFalse(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I1@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I2@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I3@"]))
        self.assertFalse(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I4@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I5@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I6@"]))

    def test_US10(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        #mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertFalse(parser.hzUserStories.marriageAfterAge(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))

if __name__ == '__main__':
    unittest.main()