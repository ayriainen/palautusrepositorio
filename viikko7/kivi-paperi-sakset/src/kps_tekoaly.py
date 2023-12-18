from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def ensimmaisenPelaajanSiirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def toisenPelaajanSiirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.annaSiirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto