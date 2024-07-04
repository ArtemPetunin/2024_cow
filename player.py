class Player:
    def __init__(self, name, player_interaction):
        self.name = name
        self.hand = Hand()
        self.captured_cards = Hand()
        self.type = player_interaction

    def choose_card(self, rows):
        return self.type.choose_card(self.hand, rows)

    def choose_row(self, rows, card):
        return self.type.choose_row(rows, card)

    def save(self):
        return {
            "name": self.name,
            "hand": self.hand.save(),
            "captured_cards": self.captured_cards.save(),
            "type": type(self.type).__name__
        }

    @classmethod
    def load(cls, data):
        if data["type"] == "Human":
            player_interaction = Human()
        elif data["type"] == "AI":
            player_interaction = AI()
        else:
            raise ValueError(f"Unknown player type: {data['type']}")
        player = cls(data["name"], player_interaction)
        player.hand = Hand.load(data["hand"])
        player.captured_cards = Hand.load(data["captured_cards"])
        return player