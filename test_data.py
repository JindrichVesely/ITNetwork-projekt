from pojisteny import Pojisteny
#Testovaci data urcena pro DEV a Debug
def napln_testovaci_data(evidence):
    evidence.pridej_pojisteneho(Pojisteny("Jan", "Novák", "35", "777123456"))
    evidence.pridej_pojisteneho(Pojisteny("Petra", "Svobodová", "29", "777654321"))
    evidence.pridej_pojisteneho(Pojisteny("Karel", "Dvořák", "42", "776111222"))
    evidence.pridej_pojisteneho(Pojisteny("Eva", "Novotná", "31", "775333444"))
    evidence.pridej_pojisteneho(Pojisteny("Martin", "Kučera", "50", "774555666"))
    evidence.pridej_pojisteneho(Pojisteny("Petr", "Pavel", "55", "774555666"))
    evidence.pridej_pojisteneho(Pojisteny("Pavel", "Petr", "56", "+420745587645"))
    evidence.pridej_pojisteneho(Pojisteny("Hulmiho", "Ukolen", "20", "774463366"))
    evidence.pridej_pojisteneho(Pojisteny("Nesera", "Navalto", "85", "770954666"))
    print("Mrtvé duše byly přidány do evidence.")
