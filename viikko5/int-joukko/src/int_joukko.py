KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise ValueError("Kapasiteetin tulee olla nollasta ylöspäin oleva kokonaisluku.")

        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon tulee olla nollasta ylöspäin oleva kokonaisluku.")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= len(self.ljono):
                self._kasvata_lista()
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def _kasvata_lista(self):
        uusi_koko = len(self.ljono) + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        kohta = self.ljono.index(n)
        self._siirra_alkiot_vasemmalle(kohta)
        self.alkioiden_lkm -= 1
        return True

    def _siirra_alkiot_vasemmalle(self, kohta):
        for i in range(kohta, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def kopioi_lista(self, vanha, uusi):
        for i in range(len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            tulos.lisaa(numero)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero not in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    def __str__(self):
        alkiot = ", ".join(map(str, self.to_int_list()))
        return f"{{{alkiot}}}"
