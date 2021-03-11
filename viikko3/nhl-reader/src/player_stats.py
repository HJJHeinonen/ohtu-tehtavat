from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, players):
        self.players = players


    def top_scorers_by_nationality(self, nationality):
        nation = nationality
        pelaajat = [player for player in self.players if player.nationality == nation]
        pelaajat = sorted(pelaajat, key = lambda player: player.points, reverse=True)
        return pelaajat