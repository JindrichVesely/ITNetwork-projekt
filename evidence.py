class Evidence:
    """
    Sprava a ukladani seznamu pojistenych

    pridej_pojisteneho(pojisteny): Pridani pojisteneho do seznamu
    vypis_vsechny(): Vypise vsechny pojistene v seznamu
    Vyhledej_pojisteneho(hledani): Vyhledá pojištěného podle jména nebo tel. cisla
    """

    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_vsechny(self):
        if not self.pojisteni:
            print("Žádný pojištěnec zatím není evidován.")
            return

        print(f"|{'Jméno':^15} | {'Prijmení':^15} | {'Věk':^5} | {'Telefon':^15}|")
        print("-------------------------------------------------------------")


        for p in self.pojisteni:
            print(f"|{p.jmeno:^15} | {p.prijmeni:^15} | {p.vek:^5} | {p.telefon:^15}|")
        print("-------------------------------------------------------------")
    def vyhledej_pojisteneho(self, hledani):
        hledani = hledani.lower()
        nalezeno = False

        for p in self.pojisteni:
            cele_jmeno = f"{p.jmeno} {p.prijmeni}".lower()
            if hledani in cele_jmeno or hledani in p.telefon:
                print(p)
                nalezeno = True

        if not nalezeno:
            print("Pojištěnec nebyl nalezen.")
