class GameInteractions:
    def __init__(self, game_state):
        self.game_state = game_state

    def run(self):
        # Main game loop
        while True:
            for player in self.game_state.players:
                card = player.choose_card(self.game_state.rows)
                taken_cards = self.game_state.play_turn((player, card))
                # Handle taken cards

    def load(self, data):
        self.game_state.load(data)

    def request_players(self):
        # Implement logic to request players and their types
        return [Player("Player 1", Human(None)), Player("Player 2", AI(None))]

    def print_rows(self, rows):
        # Implement logic to print the game rows
        pass

    def print_player(self, player, show_hand):
        # Implement logic to print the player information
        pass

# main.py
if __name__ == "__main__":
    players = GameInteractions(GameState).request_players()
    game_state = GameState(players)
    game_interactions = GameInteractions(game_state)
    game_interactions.run()
