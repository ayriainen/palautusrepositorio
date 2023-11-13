class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    #nationality arrangement
    def nationality_list(self, nationality):
        list = []
        for p in self.player_reader.reader_return():
            if p.nationality == nationality:
                list.append(p)
        return list
    
    #points arrangement
    def points(self, player):
        return player.assists + player.goals

    #nationality list call
    def top_scorers_by_nationality(self, nationality):
        player_list = self.nationality_list(nationality)
        return sorted(player_list, key=self.points, reverse=True)
