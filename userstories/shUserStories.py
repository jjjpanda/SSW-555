import unittest
from datetime import datetime
from userstories import 



def datesInFuture(date):
    """ US01: No Date can happen after current date """
    if date < datetime.today():
        return True
    else:
        print("Date ", date, "occurs in the future")
        return True

def ageGreaterThan(self): # --- ERROR WHEN DATE IS INVALID, AND THEREFORE IS A STRING ---
    if (self.deathday == "N/A"):
        upperLimit = datetime.now()
    else:
        upperLimit = self.deathday
    age = upperLimit.year - self.birthday.year - ((upperLimit.month, self.deathday.day) < (upperLimit.month, self.birthday.day))
    return True if age < 150 else False



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
    