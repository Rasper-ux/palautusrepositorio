class Summa:
    def __init__(self, logiikka, hae_syote):
        self._logiikka = logiikka
        self._hae_syote = hae_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.plus(int(self._hae_syote()))

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_arvo)


class Erotus:
    def __init__(self, logiikka, hae_syote):
        self._logiikka = logiikka
        self._hae_syote = hae_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.miinus(int(self._hae_syote()))

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_arvo)


class Nollaus:
    def __init__(self, logiikka, hae_syote):
        self._logiikka = logiikka
        self._hae_syote = hae_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.nollaa()

    def kumoa(self):
        self._logiikka.aseta_arvo(self._edellinen_arvo)

class Kumoa:
    def __init__(self, logiikka, hae_edellinen_komento):
        self._logiikka = logiikka
        self._hae_edellinen_komento = hae_edellinen_komento

    def suorita(self):
        edellinen_komento = self._hae_edellinen_komento()
        if edellinen_komento:
            edellinen_komento.kumoa()