class Evidence:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_vsechny(self):
        if not self.pojisteni:
            print("Žádný pojištěnec zatím není evidován.")
        for p in self.pojisteni:
            print(p)

    def vyhledej_pojisteneho(self, hledani):
        hledani = hledani.lower()
        nalezeno = False

        for p in self.pojisteni:
            cele_jmeno = f"{p.jmeno} {p.prijmeni}".lower()
            if hledani in cele_jmeno:
                print(p)
                nalezeno = True

        if not nalezeno:
            print("Pojištěnec nebyl nalezen.")
