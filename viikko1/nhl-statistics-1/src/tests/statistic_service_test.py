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

    def test_pelaajan_haku(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_haettua_pelaajaa_ei_olemassa(self):
        player = self.stats.search("Koivu")
        self.assertEqual(player, None)

    def test_joukkueen_pelaajat(self):
        det_players = self.stats.team("DET")
        self.assertEqual(len(det_players), 1)

    def test_eniten_pisteita(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)

    def test_eniten_syottoja(self):
        top_player = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_player[0].name, "Gretzky")

    def test_eniten_maaleja(self):
        top_player = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_player[0].name, "Lemieux")

    def test_huono_hakukriteeri(self):
        top_player = self.stats.top(1, "PENALTY")
        self.assertEqual(top_player, None)