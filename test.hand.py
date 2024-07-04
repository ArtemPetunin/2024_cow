import unittest
from unittest.mock import patch

from card import Card
from hand import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_init(self):
        self.assertEqual(self.hand.cards, [])

    def test_str(self):
        self.hand.cards = [Card(1), Card(2), Card(3)]
        self.assertEqual(str(self.hand), "1, 2, 3")

    def test_remove_card(self):
        card1 = Card(1)
        card2 = Card(2)
        self.hand.cards = [card1, card2]
        self.hand.remove_card(card1)
        self.assertEqual(self.hand.cards, [card2])

    @patch("card.Card.save")
    def test_save(self, mock_card_save):
        mock_card_save.return_value = {"number": 1}
        self.hand.cards = [Card(1), Card(2)]
        saved_data = self.hand.save()
        self.assertEqual(saved_data, [{"number": 1}, {"number": 1}])

    def test_load(self):
        data = [{"number": 1}, {"number": 2}]
        self.hand.load(data)
        self.assertEqual([card.number for card in self.hand.cards], [1, 2])

if __name__ == "__main__":
    unittest.main()
