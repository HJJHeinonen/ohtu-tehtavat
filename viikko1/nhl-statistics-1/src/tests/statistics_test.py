import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_haetaan_pelaaja(self):
        pelaaja = self.statistics.search("Semenko")
        vastaus = str(pelaaja)

        self.assertAlmostEqual(vastaus, "Semenko EDM 4 + 12 = 16")

    def test_pelaajaa_ei_loydy(self):
        pelaaja = self.statistics.search("Selanne")

        self.assertAlmostEqual(pelaaja, None)

    def test_haetaan_joukkueen_pelaajat(self):
        pelaajat = self.statistics.team("EDM")
        lista = []
        for pelaaja in pelaajat:
            tulostus = str(pelaaja)
            lista.append(tulostus)
        
        self.assertAlmostEqual(lista, ["Semenko EDM 4 + 12 = 16", "Kurri EDM 37 + 53 = 90", "Gretzky EDM 35 + 89 = 124"])

    def test_kolme_parasta_pistemiesta(self):
        pelaajat = self.statistics.top_scorers(2)
        lista = []
        for pelaaja in pelaajat:
            tulostus = str(pelaaja)
            lista.append(tulostus)

        self.assertAlmostEqual(lista, ["Gretzky EDM 35 + 89 = 124", "Lemieux PIT 45 + 54 = 99", "Yzerman DET 42 + 56 = 98"])
