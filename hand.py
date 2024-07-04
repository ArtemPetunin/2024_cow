class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ", ".join(map(str, self.cards))

    def remove_card(self, card):
        self.cards.remove(card)

    def save(self):
        return [card.save() for card in self.cards]

    def load(self, data):
        self.cards = [Card(card_data["number"]) for card_data in data]
