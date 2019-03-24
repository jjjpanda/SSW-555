import sys
sys.dont_write_bytecode = True
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mainGedcomParser as parser
import unittest

#python ./unittest/mainUnitTest.py

class TestGedcom(unittest.TestCase):
    def test_US01(self):
        print("----------US_01 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/shSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

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
   
    def test_US02(self):
        print("----------US_02 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/eaSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.eaUserStories.birthBeforeMarriage(mygedcom.individual["@I1@"], mygedcom.family["@F1@"]))
        self.assertTrue(parser.eaUserStories.birthBeforeMarriage(mygedcom.individual["@I2@"], mygedcom.family["@F1@"]))
        self.assertFalse(parser.eaUserStories.birthBeforeMarriage(mygedcom.individual["@I4@"], mygedcom.family["@F2@"]))
        self.assertTrue(parser.eaUserStories.birthBeforeMarriage(mygedcom.individual["@I8@"], mygedcom.family["@F3@"]))
        self.assertFalse(parser.eaUserStories.birthBeforeMarriage(mygedcom.individual["@I9@"], mygedcom.family["@F3@"]))

    def test_US03(self):
        print("----------US_03 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/eaSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.eaUserStories.birthBeforeDeath(mygedcom.individual["@I2@"]))
        self.assertTrue(parser.eaUserStories.birthBeforeDeath(mygedcom.individual["@I1@"]))
        self.assertTrue(parser.eaUserStories.birthBeforeDeath(mygedcom.individual["@I3@"]))
        self.assertTrue(parser.eaUserStories.birthBeforeDeath(mygedcom.individual["@I4@"]))
        self.assertTrue(parser.eaUserStories.birthBeforeDeath(mygedcom.individual["@I5@"]))

 
    def test_US04(self):
        print("----------US_04 Testing----------")
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
        print("----------US_05 Testing----------")
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
        print("----------US_06 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertFalse(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertTrue(parser.hzUserStories.divorceBeforeDeath(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))

    def test_US07(self):
        print("----------US_07 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/shSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I1@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I2@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I3@"]))
        self.assertFalse(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I4@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I5@"]))
        self.assertTrue(parser.shUserStories.ageGreaterThan(mygedcom.individual["@I6@"]))

    def test_US08(self):
        print("----------US_08 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/shSprint2test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.shUserStories.birthBeforeMarriage(mygedcom.individual["@I9@"], mygedcom.family[mygedcom.individual["@I9@"].famc]))
        self.assertFalse(parser.shUserStories.birthBeforeMarriage(mygedcom.individual["@I5@"], mygedcom.family[mygedcom.individual["@I5@"].famc]))
        self.assertTrue(parser.shUserStories.birthBeforeMarriage(mygedcom.individual["@I6@"], mygedcom.family[mygedcom.individual["@I6@"].famc]))
        self.assertFalse(parser.shUserStories.birthBeforeMarriage(mygedcom.individual["@I1@"], mygedcom.family[mygedcom.individual["@I1@"].famc]))
        self.assertTrue(parser.shUserStories.birthBeforeMarriage(mygedcom.individual["@I7@"], mygedcom.family[mygedcom.individual["@I7@"].famc]))

    def test_US09(self):
        print("----------US_09 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/shSprint2test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.shUserStories.birthBeforeDeath(mygedcom.individual["@I1@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I1@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I1@"].famc].wife]))
        self.assertTrue(parser.shUserStories.birthBeforeDeath(mygedcom.individual["@I5@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I5@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I5@"].famc].wife]))
        self.assertFalse(parser.shUserStories.birthBeforeDeath(mygedcom.individual["@I6@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I6@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I6@"].famc].wife]))
        self.assertFalse(parser.shUserStories.birthBeforeDeath(mygedcom.individual["@I7@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I7@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I7@"].famc].wife]))
        self.assertTrue(parser.shUserStories.birthBeforeDeath(mygedcom.individual["@I9@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I9@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I9@"].famc].wife]))

    def test_US10(self):
        print("----------US_10 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/hzSprint1test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.hzUserStories.marriageAfterFourteen(mygedcom.family["@F1@"], mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(parser.hzUserStories.marriageAfterFourteen(mygedcom.family["@F2@"], mygedcom.individual[mygedcom.family["@F2@"].husband], mygedcom.individual[mygedcom.family["@F2@"].wife]))
        self.assertFalse(parser.hzUserStories.marriageAfterFourteen(mygedcom.family["@F3@"], mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertTrue(parser.hzUserStories.marriageAfterFourteen(mygedcom.family["@F4@"], mygedcom.individual[mygedcom.family["@F4@"].husband], mygedcom.individual[mygedcom.family["@F4@"].wife]))
        self.assertFalse(parser.hzUserStories.marriageAfterFourteen(mygedcom.family["@F5@"], mygedcom.individual[mygedcom.family["@F5@"].husband], mygedcom.individual[mygedcom.family["@F5@"].wife]))

    def test_US11(self):
        print("----------US_11 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/eaSprint2test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.eaUserStories.noBigamy(mygedcom.family["@F1@"], mygedcom.family["@F2@"]))
        self.assertTrue(parser.eaUserStories.noBigamy(mygedcom.family["@F3@"], mygedcom.family["@F4@"]))
        self.assertTrue(parser.eaUserStories.noBigamy(mygedcom.family["@F1@"], "N/A"))
        self.assertTrue(parser.eaUserStories.noBigamy("N/A", mygedcom.family["@F4@"]))
        self.assertFalse(parser.eaUserStories.noBigamy(mygedcom.family["@F3@"], mygedcom.family["@F5@"]))
    
    def test_US12(self):
        print("----------US_12 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/eaSprint2test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertFalse(parser.eaUserStories.parentsNotTooOld(mygedcom.individual["@I1@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I1@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I1@"].famc].wife]))
        self.assertFalse(parser.eaUserStories.parentsNotTooOld(mygedcom.individual["@I5@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I5@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I5@"].famc].wife]))
        self.assertFalse(parser.eaUserStories.parentsNotTooOld(mygedcom.individual["@I6@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I6@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I6@"].famc].wife]))
        self.assertFalse(parser.eaUserStories.parentsNotTooOld(mygedcom.individual["@I7@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I7@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I7@"].famc].wife]))
        self.assertTrue(parser.eaUserStories.parentsNotTooOld(mygedcom.individual["@I9@"], mygedcom.individual[mygedcom.family[mygedcom.individual["@I9@"].famc].husband], mygedcom.individual[mygedcom.family[mygedcom.individual["@I9@"].famc].wife]))
    
    def test_US14(self):
        print("----------US_14 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/hzSprint2test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.hzUserStories.noMoreThanQuintuplets(mygedcom.family["@F1@"], mygedcom.individual))
        self.assertFalse(parser.hzUserStories.noMoreThanQuintuplets(mygedcom.family["@F2@"], mygedcom.individual))
        self.assertTrue(parser.hzUserStories.noMoreThanQuintuplets(mygedcom.family["@F3@"], mygedcom.individual))

    def test_US15(self):
        print("----------US_15 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/hzSprint2test.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.hzUserStories.fewerThanFifteenSiblings(mygedcom.family["@F1@"]))
        self.assertFalse(parser.hzUserStories.fewerThanFifteenSiblings(mygedcom.family["@F2@"]))
        self.assertTrue(parser.hzUserStories.fewerThanFifteenSiblings(mygedcom.family["@F3@"]))

    def test_US18(self):
        print("----------US_18 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/superMessedUpFamily.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.jpUserStories.noIncest(mygedcom.family["@F1@"].id, mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(parser.jpUserStories.noIncest(mygedcom.family["@F3@"].id, mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertFalse(parser.jpUserStories.noIncest(mygedcom.family["@F7@"].id, mygedcom.individual[mygedcom.family["@F7@"].husband], mygedcom.individual[mygedcom.family["@F7@"].wife]))

    def test_US21(self):
        print("----------US_21 Testing----------")
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("./gedcoms/superMessedUpFamily.ged")
        parser.gedcom_categorizer(valid, mygedcom)
        mygedcom.genTables(mygedcom.individual, mygedcom.family)

        self.assertTrue(parser.jpUserStories.correctGender(mygedcom.family["@F1@"].id, mygedcom.individual[mygedcom.family["@F1@"].husband], mygedcom.individual[mygedcom.family["@F1@"].wife]))
        self.assertTrue(parser.jpUserStories.correctGender(mygedcom.family["@F3@"].id, mygedcom.individual[mygedcom.family["@F3@"].husband], mygedcom.individual[mygedcom.family["@F3@"].wife]))
        self.assertFalse(parser.jpUserStories.correctGender(mygedcom.family["@F7@"].id, mygedcom.individual[mygedcom.family["@F7@"].husband], mygedcom.individual[mygedcom.family["@F7@"].wife]))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestGedcom))