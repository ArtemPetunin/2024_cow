import unittest
from unittest.mock import patch, Mock, call
from io import StringIO

from human import Human
from hand import Hand
from card import Card

class TestHuman(unittest.TestCase):
    @patch('builtins.input', side_effect=['7', '2'])
    def test_choose_card(self, mock_input):
        hand = Hand([Card(1), Card(7), Card(10)])
        rows = []
        human = Human()
        with patch('sys.stdout', new=StringIO()):
            chosen_card = human.choose_card(hand, rows)
        self.assertEqual(chosen_card.number, 7)

    @patch('builtins.input', side_effect=['3', 'a', '1'])
    def test_choose_row(self, mock_input):
        rows = [[], [Card(3)], [Card(5), Card(9)]]
        card = Card(7)
        human = Human()
        with patch('sys.stdout', new=StringIO()):
            chosen_row = human.choose_row(rows, card)
        self.assertEqual(chosen_row, 1)

    def test_choose_card_invalid_input(self):
        hand = Hand([Card(1), Card(7), Card(10)])
        rows = []
        human = Human()
        with patch('sys.stdout', new=StringIO()), \
             patch('builtins.input', side_effect=['a', '5', '7']):
            chosen_card = human.choose_card(hand, rows)
        self.assertEqual(chosen_card.number, 7)

    def test_choose_row_invalid_input(self):
        rows = [[], [Card(3)], [Card(5), Card(9)]]
        card = Card(7)
        human = Human()
        with patch('sys.stdout', new=StringIO()), \
             patch('builtins.input', side_effect=['a', '5', '2']):
            chosen_row = human.choose_row(rows, card)
        self.assertEqual(chosen_row, 1)

if __name__ == "__main__":
    unittest.main()
