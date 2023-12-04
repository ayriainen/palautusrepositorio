class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores ={player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        self.scores[player_name] += 1

    def get_score(self):
        if self.is_equal():
            return "Deuce" if self.scores[self.player1_name] >= 3 else f"{self.SCORE_NAMES[self.scores[self.player1_name]]}-All"
        if self.is_normal():
            return f"{self.SCORE_NAMES[self.scores[self.player1_name]]}-{self.SCORE_NAMES[self.scores[self.player2_name]]}"
        return self.advantage_or_win()
    
    def is_equal(self):
        return self.scores[self.player1_name] == self.scores[self.player2_name]

    def is_normal(self):
        return self.scores[self.player1_name] < 4 and self.scores[self.player2_name] < 4

    def advantage_or_win(self):
        difference = self.scores[self.player1_name] - self.scores[self.player2_name]
        
        if abs(difference) == 1:
            return f"Advantage {self.player1_name if difference > 0 else self.player2_name}"
        return f"Win for {self.player1_name if difference > 0 else self.player2_name}"