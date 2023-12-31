class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = [arvo]

    def miinus(self, operandi):
        self._historia.append(self._arvo)
        self._arvo -= operandi

    def plus(self, operandi):
        self._historia.append(self._arvo)
        self._arvo += operandi

    def nollaa(self):
        self._historia.append(self._arvo)
        self._arvo = 0
    
    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def kumoa(self):
        if len(self._historia) > 0:
            self._arvo = self._historia.pop()
        else:
            self._arvo = 0

    def arvo(self):
        return self._arvo
