class Pojisteny:
    #Instance pojistence
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    #Návrat žádosti o pojištěnce
    def __str__(self):
        return f"Jméno: {self.jmeno:} {self.prijmeni:} Věk: {self.vek:} Tel.:{self.telefon}"

