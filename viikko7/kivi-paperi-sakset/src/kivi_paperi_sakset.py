from tuomari import Tuomari

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self.ensimmaisenPelaajanSiirto()
            if not self.onkoOKSiirto(ekan_siirto):
                break

            tokan_siirto = self.toisenPelaajanSiirto(ekan_siirto)
            if not self.onkoOKSiirto(tokan_siirto):
                break

            tuomari.kirjaaSiirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def ensimmaisenPelaajanSiirto(self):
        raise NotImplementedError("Alaluokkavirhe")
    
    def toisenPelaajanSiirto(self, ensimmaisen_siirto):
        raise NotImplementedError("Alaluokkavirhe")
    
    def onkoOKSiirto(self, siirto):
        return siirto in ["k", "p", "s"]