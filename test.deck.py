import unittest
from unittest.mock import Mock

from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
    def test_init(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 103)
        for card in deck.cards:
            self.assertIsInstance(card, Card)

    def test_draw(self):
        mock_card = Mock(spec=Card)
        deck = Deck(mock_card)
        self.assertIs(deck.draw(), mock_card)
        self.assertEqual(len(deck.cards), 102)

    def test_shuffle(self):
        deck = Deck()
        original_cards = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_cards)

    def test_save(self):
        deck = Deck()
        saved_data = deck.save()
        self.assertEqual(saved_data, [card.save() for card in deck.cards])

    def test_load(self):
        saved_data = [{"number": 1}, {"number": 2}, {"number": 3}]
        deck = Deck.load(saved_data)
        self.assertEqual([card.number for card in deck.cards], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
