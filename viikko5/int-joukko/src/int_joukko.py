class IntJoukko:
    #turhat kapasiteetti ja kasvatuskoko, että sai yhden testin toimimaan
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.lista = []

    def kuuluu(self, n):
        return n in self.lista

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lista.append(n)

    def poista(self, n):
        if self.kuuluu(n):
            self.lista.remove(n)
            return True
        return False

    def mahtavuus(self):
        return len(self.lista)

    def to_int_list(self):
        return self.lista

    #näissä loin uudet IntJoukot kuten oli aiemmassa

    @staticmethod
    def yhdiste(a, b):
        c = IntJoukko()
        for n in a.to_int_list():
            c.lisaa(n)
        for n in b.to_int_list():
            c.lisaa(n)
        return c

    @staticmethod
    def leikkaus(a, b):
        c = IntJoukko()
        for n in a.to_int_list():
            if b.kuuluu(n):
                c.lisaa(n)
        return c

    @staticmethod
    def erotus(a, b):
        c = IntJoukko()
        for n in a.to_int_list():
            c.lisaa(n)
        for n in b.to_int_list():
            c.poista(n)
        return c

    def __str__(self):
        return "{" + ", ".join(str(i) for i in self.lista) + "}"
