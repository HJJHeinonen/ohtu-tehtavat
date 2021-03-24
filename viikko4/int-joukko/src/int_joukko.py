KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Virheellinen kasvatuskoko")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = []

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.ljono:
            return True
        else:
            return False

    def lisaa(self, luku):
        if len(self.ljono) == self.kapasiteetti:
            self.kapasiteetti += self.kasvatuskoko
        if self.kuuluu(luku):
            return False
        else:
            self.ljono.insert(0,luku)
            self.alkioiden_lkm += 1
            return True

    def poista(self, luku):
        if luku in self.ljono:
            self.ljono.remove(luku)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        taulu_x = IntJoukko()
        taulu_a = joukko_a.to_int_list()
        taulu_b = joukko_b.to_int_list()
        for luku in taulu_a:
            taulu_x.lisaa(luku)
        for luku in taulu_b:
            taulu_x.lisaa(luku)
        return taulu_x

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        taulu_y = IntJoukko()
        taulu_a = joukko_a.to_int_list()
        taulu_b = joukko_b.to_int_list()
        for luku in taulu_a:
            if luku in taulu_b:
                taulu_y.lisaa(luku)
        return taulu_y

    @staticmethod
    def erotus(joukko_a, joukko_b):
        taulu_z = IntJoukko()
        taulu_a = joukko_a.to_int_list()
        taulu_b = joukko_b.to_int_list()
        for luku in taulu_a:
            if luku not in taulu_b:
                taulu_z.lisaa(luku)
        return taulu_z

    def __str__(self):
        lista = sorted(self.ljono, reverse=True)
        tuloste = str(lista)[1:-1] 
        return "{"f"{tuloste}""}"