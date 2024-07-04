class Row:
    def __init__(self):
        self.cards = []

    def put_card(self, card):
        self.cards.append(card)
        self.cards.sort(key=lambda x: x.number)

    def take_cards(self):
        taken_cards = self.cards[:]
        self.cards = []
        return taken_cards

    def save(self):
        return {"cards": [{"number": card.number, "score": card.score} for card in self.cards]}

    @classmethod
    def load(cls, data):
        row = cls()
        row.cards = [Card(card_data["number"], card_data["score"]) for card_data in data["cards"]]
        return row