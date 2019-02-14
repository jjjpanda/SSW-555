import unittest
from datetime import datetime
import mainGedcomParser as parser



def datesInFuture(date):
    """ US01: No Date can happen after current date """
    if date < datetime.today():
        return True
    else:
        print("Date ", date, "occurs in the future")
        return True

def ageGreaterThan(individual): # --- ERROR WHEN DATE IS INVALID, AND THEREFORE IS A STRING ---
    if (individual.deathday == "N/A"):
        upperLimit = datetime.now()
    else:
        upperLimit = individual.deathday
    age = upperLimit.year - individual.birthday.year - ((upperLimit.month, individual.deathday.day) < (upperLimit.month, individual.birthday.day))
    if age < 150:
        return True
    else:
        print("this individual lives more than 150 years") 
        return False



class SprintOneTest(unittest.TestCase):
    """
    @I1@ lives longer than 150
    @I2@ is born and dies in the future 
    """
    def test_datesInFuture(self):
        """ Tests US01: No Date can happen after current date """
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("shSprint1Test.ged")
        parser.gedcom_categorizer(valid, mygedcom)

        self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].deathday))
        self.assertFalse(datesInFuture(mygedcom.individual["@I1@"].birthday))
        self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].birthday))

    def test_ageGreaterThan(self):
        mygedcom = parser.GedcomFile()
        valid = parser.gedcom_cleaner("shSprint1Test.ged")
        parser.gedcom_categorizer(valid, mygedcom)

        self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].deathday))
        self.assertFalse(datesInFuture(mygedcom.individual["@I1@"].birthday))
        self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].birthday))
   


if __name__ == '__main__':
    # main()
    unittest.main(exit = False, verbosity = 2)
    