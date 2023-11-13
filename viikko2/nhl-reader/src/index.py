from player import Player
from playerstats import PlayerStats
from playerreader import PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    #player name, team, goals + assists = points, penalties, games
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
