from kivi_paperi_sakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def ensimmaisenPelaajanSiirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def toisenPelaajanSiirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
