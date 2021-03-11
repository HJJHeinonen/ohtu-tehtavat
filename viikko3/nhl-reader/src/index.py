from player_reader import PlayerReader
from player_stats import PlayerStats
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url).get_players()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    time = datetime.now()
    print(f"Players from FIN {time}")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
