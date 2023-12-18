from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def ensimmaisenPelaajanSiirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def toisenPelaajanSiirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.annaSiirto()
        self.tekoaly.asetaSiirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {siirto}")
        return siirto