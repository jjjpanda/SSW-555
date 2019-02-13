import unittest
from datetime import datetime


def stringToDate(strInput):
    """creates datetime objects from the string inputs. 
    If date happens in the future it prints an error message (US01).
    If date is given in the wrong format, it prints an error message. 
    """
    try:
        date = datetime.strptime(strInput, "%d %b %Y")
        if date < datetime.today():
            return date
        else:
            print("Invalid date", strInput, "happens in the future")
            return("FutureDate")
    except ValueError: # ---FIX THIS EXCEPTION, THROWING OFF ERROR WHEN CALCULATING AGE ---
        print("the input", strInput, "is not in the expected format dd mmm yyyy")
        return strInput

def getAge(self): # --- ERROR WHEN DATE IS INVALID, AND THEREFORE IS A STRING ---
    if (self.deathday == "N/A"):
        currentDate = datetime.now()
        age = currentDate.year - self.birthday.year - ((currentDate.month, currentDate.day) < (self.birthday.month, self.birthday.day))
    else:
        age = self.deathday.year - self.birthday.year - ((self.deathday.month, self.deathday.day) < (self.birthday.month, self.birthday.day))
    return age if age < 150 else "Age is over 150 years" 

class GedcomTest(unittest.TestCase):
    def test_us01(self):
        """ Tests that all dates happen before current date """
        # self.assertEqual(str(stringToDate("3 AUG 1942")), "1942-08-03 00:00:00")
        self.assertEqual(stringToDate("3 AUG 2042"), "FutureDate")
        self.assertEqual(stringToDate("12 FEB 2022"), "FutureDate")
        # with self.assertRaises(ValueError):
        #     stringToDate("35 SEPTEMBER 2011")
    # def test_us07(self):
    #     self.assertEqual(getAge)   


if __name__ == '__main__':
    unittest.main(exit = False, verbosity = 2)
    