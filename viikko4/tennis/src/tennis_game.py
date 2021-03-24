class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_library = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1    

    def players_are_even(self):
        if self.player1_score <  4:
            return f"{self.score_library[self.player1_score]}-All"          
        else:
            return "Deuce"            

    def one_player_is_leading(self):
        if self.player1_score < 4 and self.player2_score < 4:
            return f"{self.score_library[self.player1_score]}-{self.score_library[self.player2_score]}"
        else:
            if self.player1_score - self.player2_score == 1:
                return f"Advantage player1"
            else:
                return f"Advantage player2"

    def winner(self):
        if self.player1_score - self.player2_score >= 2:
            return f"Win for player1"
        else:
            return f"Win for player2"

    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self.players_are_even()
        if self.player1_score != self.player2_score:
            score = self.one_player_is_leading()
        if self.player1_score - self.player2_score >= 2 and self.player1_score > 3 or self.player2_score - self.player1_score >= 2 and self.player2_score > 3: 
            score = self.winner()
        return score

