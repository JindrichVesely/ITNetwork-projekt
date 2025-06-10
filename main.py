import re
from pojisteny import Pojisteny
from evidence import Evidence
from test_data import napln_testovaci_data #TESTOVACÍ DATA, ODEBRAT a smazat test_data.py

def pokracuj():
    input("\nPokračujte libovolnou klávesou...")

#Kontroluje vstup zda neni prazdny
def kontrola_vstupu(prompt):
    while True:
        hodnota = input(prompt).strip()
        if hodnota:
            return hodnota
        print("Musíte zadat text.")
#Kontroluje vek, zda je v rozmezi 1-119
def kontrola_vek(prompt):
    while True:
        vek_str = input(prompt).strip()
        if vek_str.isdigit() and 0 < int(vek_str) < 120:
            return int(vek_str)
        print("Zadejte prosím platný věk:")

#Kontrola ze cislo obsahuje pouze cisla a znamenko +, ktere muze byt pouze na zacatku
#a kontrola delky
def kontrola_telefon(prompt):
    while True:
        telefon = input(prompt).strip()
        pattern = r"\+?\d{9,13}$"
        if re.fullmatch(pattern, telefon):
            return telefon
        print("Telefon musí obsahovat pouze čísla a znaménko +.")

def main():
    evidence = Evidence()
    #Hlavni menu
    while True:
        print("╔════════════════════════════════╗")
        print("║    Evidence pojištěných        ║")
        print("╠════════════════════════════════╣")
        print("║ Vyberte si akci:               ║")
        print("║ 1 - Přidat nového pojištěnce   ║")
        print("║ 2 - Vypsat všechny pojištěné   ║")
        print("║ 3 - Vyhledat pojištěnce        ║")
        print("║ 4 - Konec                      ║")
        print("╠════════════════════════════════╣")
        print("║\033[91m 8 - Načíst testovací data \033[0m     ║")  #TESTOVACÍ DATA, ODEBRAT a smazat test_data.py
        print("╚════════════════════════════════╝ \n")

        volba = input()
        
        match volba:
            #formular pro pridani pojistence
            case "1":
                jmeno = kontrola_vstupu("Zadejte jméno pojištěného: ")
                prijmeni = kontrola_vstupu("Zadejte příjmení pojištěného: ")
                vek = kontrola_vek("Zadejte věk pojištěného: ")
                telefon = kontrola_telefon("Zadejte telefonní číslo pojištěného bez předvolby: ")
                evidence.pridej_pojisteneho(Pojisteny(jmeno, prijmeni, vek, telefon))
                print("Karta pojištěnce byla vytvořena.")
                pokracuj()
                input()

            #formular pro vypsani vsech pojistenych
            case "2":
                evidence.vypis_vsechny()
                pokracuj()

            #formular pro vyhledani pojisteneho
            case "3":
                hledani = kontrola_vstupu("Zadejte jméno, příjmení nebo oboje: ")
                evidence.vyhledej_pojisteneho(hledani)
                pokracuj()

            #Ukonceni programu
            case "4":
                break

            # TESTOVACÍ DATA, ODEBRAT a smazat test_data.py
            case "8":
                napln_testovaci_data(evidence)
                pokracuj()

            case _:
                print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()