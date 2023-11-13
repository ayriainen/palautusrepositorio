class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']
    
    #return list format
    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name:20} {self.team:5} {self.goals:2} + {self.assists:2} = {points:4} | {self.penalties:2} | {self.games:2}"
