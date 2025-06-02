from pojisteny import Pojisteny
from evidence import Evidence

def kontrola_vstupu(prompt):
    while True:
        hodnota = input(prompt).strip()
        if hodnota:
            return hodnota
        print("Musíte zadat text.")

def main():
    evidence = Evidence()

    while True:
        print("============================")
        print("Evidence pojištěných")
        print("============================")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěnce")
        print("4 - Konec")


        volba = input()
        if volba == "1":
            jmeno = kontrola_vstupu("Zadejte jméno pojištěného: ")
            prijmeni = kontrola_vstupu("Zadejte příjmení pojištěného: ")
            vek = kontrola_vstupu("Zadejte věk pojištěného: ")
            telefon = kontrola_vstupu("Zadejte telefonní číslo pojištěného: ")
            evidence.pridej_pojisteneho(Pojisteny(jmeno, prijmeni, vek, telefon))
            print("Karta pojištěnce byla vytvořena. Pokračujte libovolnou klávesou...")
            input()

        elif volba == "2":
            evidence.vypis_vsechny()
            input("\nPokračujte libovolnou klávesou...")

        elif volba == "3":
            jmeno = kontrola_vstupu("Zadejte jméno pojištěného: ")
            prijmeni = kontrola_vstupu("Zadejte příjmení: ")
            evidence.vyhledej_pojisteneho(jmeno, prijmeni)
            input("Pokračujte libovolnou klávesou...")

        elif volba == "4":
            break

        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()
