class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            [player for player in self.players if player.nationality == nationality],
            key=lambda player: player.points,
            reverse=True
        )


