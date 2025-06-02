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

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        nalezeno = False
        for p in self.pojisteni:
            if p.jmeno.lower() == jmeno.lower() and p.prijmeni.lower() == prijmeni.lower():
                print(p)
                nalezeno = True1
        if not nalezeno:
            print("Pojištěnec nebyl nalezen.")
