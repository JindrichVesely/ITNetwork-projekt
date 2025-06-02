from pojisteny import Pojisteny
from evidence import Evidence
from test_data import napln_testovaci_data #TESTOVACÍ DATA, ODEBRAT a smazat test_data.py

#Kontroluje vstup zda neni prazdny
def kontrola_vstupu(prompt):
    while True:
        hodnota = input(prompt).strip()
        if hodnota:
            return hodnota
        print("Musíte zadat text.")

def main():
    evidence = Evidence()
    #Hlavni menu
    while True:
        print("============================")
        print("Evidence pojištěných")
        print("============================")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěnce")
        print("4 - Konec")
        print("============================")
        print("\033[91m8 - Načíst testovací data\033[0m")  #TESTOVACÍ DATA, ODEBRAT a smazat test_data.py

        #formular pro pridani pojistence
        volba = input()
        if volba == "1":
            jmeno = kontrola_vstupu("\nZadejte jméno pojištěného: ")
            prijmeni = kontrola_vstupu("Zadejte příjmení pojištěného: ")
            vek = kontrola_vstupu("Zadejte věk pojištěného: ")
            telefon = kontrola_vstupu("Zadejte telefonní číslo pojištěného: ")
            evidence.pridej_pojisteneho(Pojisteny(jmeno, prijmeni, vek, telefon))
            print("Karta pojištěnce byla vytvořena. Pokračujte libovolnou klávesou...")
            input()

        #formular pro vypsani vsech pojistenych
        elif volba == "2":
            evidence.vypis_vsechny()
            input("Pokračujte libovolnou klávesou...")

        #formular pro vyhledani pojisteneho
        elif volba == "3":
            hledani = kontrola_vstupu("Zadejte jméno, příjmení nebo oboje: ")
            evidence.vyhledej_pojisteneho(hledani)
            input("Pokračujte libovolnou klávesou...")

        #Ukonceni programu
        elif volba == "4":
            break

        # TESTOVACÍ DATA, ODEBRAT a smazat test_data.py
        elif volba == "8":
            napln_testovaci_data(evidence)
            input("Testovací data byla načtena. Pokračujte libovolnou klávesou...")

        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()
