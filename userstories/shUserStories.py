import unittest
from datetime import datetime


def IDatesInFuture(individuals):
    """ US01: No Date in individuals can happen after current date """
    for date in [individuals.birthday, individuals.deathday]:
        if date != "N/A":
            if date < datetime.today():
                return True
            else:
                print("ERROR: INDIVIDUAL: US01: Date", date, "occurs in the future")
                return False
def FDatesInFuture(families):
    """ US01: No Date in a family can happen after current date """
    for date in [families.marriage, families.divorce]:
        if date != "N/A":
            if date < datetime.today():
                return True
            else:
                print("ERROR: FAMILY: US01: Date", date, "occurs in the future")
                return False

def ageGreaterThan(individual): # --- ERROR WHEN DATE IS INVALID, AND THEREFORE IS A STRING ---
    if (individual.deathday == "N/A"):
        currentDate = datetime.now()
        age = currentDate.year - individual.birthday.year - ((currentDate.month, currentDate.day) < (individual.birthday.month, individual.birthday.day))
    else:
        age = individual.deathday.year - individual.birthday.year - ((individual.deathday.month, individual.deathday.day) < (individual.birthday.month, individual.birthday.day))
    if age < 150:
        return True
    else:
        print("ERROR: INDIVIDUAL: US07", individual.name, "with ID", individual.id, "lives more than 150 years. Birth date is", individual.birthday.date()) 
        return False

def test(individuals, families):
    for indi in individuals.values():
        ageGreaterThan(indi)
        IDatesInFuture(indi)
    for fam in families.values():
        FDatesInFuture(fam)


# class SprintOneTest(unittest.TestCase):
#     """
#     @I1@ lives longer than 150
#     @I2@ is born and dies in the future 
#     """
#     def test_datesInFuture(self):
#         """ Tests US01: No Date can happen after current date """
#         mygedcom = parser.GedcomFile()
#         valid = parser.gedcom_cleaner("shSprint1Test.ged")
#         parser.gedcom_categorizer(valid, mygedcom)

#         self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].deathday))
#         self.assertFalse(datesInFuture(mygedcom.individual["@I1@"].birthday))
#         self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].birthday))

#     def test_ageGreaterThan(self):
#         mygedcom = parser.GedcomFile()
#         valid = parser.gedcom_cleaner("shSprint1Test.ged")
#         parser.gedcom_categorizer(valid, mygedcom)

#         self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].deathday))
#         self.assertFalse(datesInFuture(mygedcom.individual["@I1@"].birthday))
#         self.assertTrue(datesInFuture(mygedcom.individual["@I2@"].birthday))
   


if __name__ == '__main__':
    # main()
    unittest.main(exit = False, verbosity = 2)
    