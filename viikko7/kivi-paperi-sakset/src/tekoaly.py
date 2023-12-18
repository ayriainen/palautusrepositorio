class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def annaSiirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"

    def asetaSiirto(self, siirto):
        # ei tehdä mitään
        pass
