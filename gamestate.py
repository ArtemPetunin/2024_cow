class GameState:
    def __init__(self, players):
        self.players = players
        self.rows = [Row() for _ in range(len(players))]

    def play_card(self, card):
        for row in self.rows:
            taken_cards = row.take_cards(card)
            if taken_cards:
                return taken_cards
        return []

    def play_turn(self, player_card_pair):
        player, card = player_card_pair
        taken_cards = self.play_card(card)
        player.hand.remove_card(card)
        row_index = player.choose_row(self.rows, card)
        self.rows[row_index].put_card(card)
        return taken_cards

    def save(self):
        return {
            "players": [player.save() for player in self.players],
            "rows": [row.save() for row in self.rows]
        }

    def load(self, data):
        self.players = [Player(player_data["name"], PLAYER_TYPES[player_data["type"]](None)) for player_data in data["players"]]
        self.rows = [Row() for _ in range(len(self.players))]
        for row_data, row in zip(data["rows"], self.rows):
            row.load(row_data)
        for player, player_data in zip(self.players, data["players"]):
            player.hand.load(player_data["hand"])

from abc import ABC, abstractmethod