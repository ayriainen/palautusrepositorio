import unittest
from statistics_service import StatisticsService, SortBy
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_ei_loyda_pelaajaa(self):
        pelaaja = self.stats.search("Koivu")

        self.assertIsNone(pelaaja)

    def test_search_loytaa_pelaajan(self):
        pelaaja = self.stats.search("Kurri")

        self.assertIsNotNone(pelaaja)

        self.assertEqual(pelaaja.name, "Kurri")

    def test_team_jolla_ei_pelaajia(self):
        pelaajat = self.stats.team("JOK")

        self.assertEqual(len(pelaajat), 0)

    def test_team_jolla_on_pelaajia(self):
        pelaajat = self.stats.team("EDM")

        self.assertEqual(len(pelaajat), 3)

        self.assertTrue(all(pelaaja.team == "EDM" for pelaaja in pelaajat))

    def test_top_oikea_maara(self):
        parhaat = self.stats.top(2)

        self.assertEqual(len(parhaat), 2)

    def test_top_kaikki(self):
        parhaat = self.stats.top(5)

        self.assertEqual(len(parhaat), 5)

    def test_top_sort_by_points(self):
        pelaajat = self.stats.top(5)

        self.assertEqual(pelaajat[0].name, "Gretzky")

        self.assertEqual(pelaajat[1].name, "Lemieux")

        self.assertEqual(pelaajat[2].name, "Yzerman")

        self.assertEqual(pelaajat[3].name, "Kurri")

        self.assertEqual(pelaajat[4].name, "Semenko")

    def test_top_sort_by_goals(self):
        pelaajat = self.stats.top(5, SortBy.GOALS)

        self.assertEqual(pelaajat[0].name, "Lemieux")

        self.assertEqual(pelaajat[1].name, "Yzerman")

        self.assertEqual(pelaajat[2].name, "Kurri")

        self.assertEqual(pelaajat[3].name, "Gretzky")

        self.assertEqual(pelaajat[4].name, "Semenko")

    def test_top_sort_by_assists(self):
        pelaajat = self.stats.top(5, SortBy.ASSISTS)

        self.assertEqual(pelaajat[0].name, "Gretzky")

        self.assertEqual(pelaajat[1].name, "Yzerman")

        self.assertEqual(pelaajat[2].name, "Lemieux")

        self.assertEqual(pelaajat[3].name, "Kurri")

        self.assertEqual(pelaajat[4].name, "Semenko")
    
    def test_top_oikea_jarjestys(self):
        parhaat = self.stats.top(2)

        self.assertTrue(all(parhaat[luku].points >= parhaat[luku + 1].points for luku in range(len(parhaat) - 1)))

    def test_top_liian_monta(self):
        parhaat = self.stats.top(8)

        self.assertEqual(len(parhaat), 5)

    def test_top_miinus(self):
        parhaat = self.stats.top(-1)

        self.assertEqual(len(parhaat), 0)

