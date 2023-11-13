import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.players_sort()

    #players added
    def players_sort(self):
        response = requests.get(self.url).json()
        for player_stats in response:
            self.players.append(Player(player_stats))
        
    #player reader get
    def reader_return(self):
        return self.players
    
