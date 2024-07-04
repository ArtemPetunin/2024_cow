import unittest
from unittest.mock import Mock, patch

from player import Player
from hand import Hand
from human import Human
from ai import AI

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player("Alice", Human())
        self.assertEqual(player.name, "Alice")
        self.assertIsInstance(player.hand, Hand)
        self.assertIsInstance(player.captured_cards, Hand)
        self.assertIsInstance(player.type, Human)

    @patch("human.Human.choose_card")
    def test_choose_card(self, mock_choose_card):
        mock_choose_card.return_value = Card(7)
        player = Player("Bob", Human())
        player.hand.cards = [Card(1), Card(2), Card(7)]
        chosen_card = player.choose_card([])
        self.assertEqual(chosen_card.number, 7)

    @patch("human.Human.choose_row")
    def test_choose_row(self, mock_choose_row):
        mock_choose_row.return_value = 2
        player = Player("Charlie", Human())
        rows = [[], [Card(3)], [Card(5), Card(9)]]
        chosen_row = player.choose_row(rows, Card(7))
        self.assertEqual(chosen_row, 2)

    def test_save(self):
        player = Player("David", AI())
        player.hand.cards = [Card(1), Card(2)]
        player.captured_cards.cards = [Card(3), Card(4)]
        saved_data = player.save()
        self.assertEqual(saved_data, {
            "name": "David",
            "hand": [{"number": 1}, {"number": 2}],
            "captured_cards": [{"number": 3}, {"number": 4}],
            "type": "AI"
        })

    def test_load(self):
        data = {
            "name": "Emily",
            "hand": [{"number": 5}, {"number": 8}],
            "captured_cards": [{"number": 3}, {"number": 9}],
            "type": "Human"
        }
        loaded_player = Player.load(data)
        self.assertEqual(loaded_player.name, "Emily")
        self.assertEqual([card.number for card in loaded_player.hand.cards], [5, 8])
        self.assertEqual([card.number for card in loaded_player.captured_cards.cards], [3, 9])
        self.assertIsInstance(loaded_player.type, Human)

if __name__ == "__main__":
    unittest.main()
