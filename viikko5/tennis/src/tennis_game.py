class TennisGame:
    POINTS_TO_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):

        if self.is_score_even():
            score = self.game_even()
        elif self.is_endgame():
            score = self.game_advantage()
        else:
            score = self.whichever_leads()

        return score

    def is_score_even(self):
        return self.m_score1 == self.m_score2

    def is_endgame(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def game_even(self):
        if self.m_score1 < len(self.POINTS_TO_NAMES)-1:
            return f"{self.POINTS_TO_NAMES[self.m_score1]}-All"
        return "Deuce"

    def game_advantage(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def whichever_leads(self):
        player1_score_name = self.POINTS_TO_NAMES[self.m_score1]
        player2_score_name = self.POINTS_TO_NAMES[self.m_score2]
        return f"{player1_score_name}-{player2_score_name}"

