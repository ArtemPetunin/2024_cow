import unittest
from unittest.mock import patch, Mock
import random

from ai import AI
from hand import Hand
from card import Card

class TestAI(unittest.TestCase):
    @patch('random.choice')
    def test_choose_card(self, mock_random_choice):
        mock_random_choice.return_value = Card(7)
        hand = Hand([Card(1), Card(7), Card(10)])
        rows = []
        ai = AI()
        chosen_card = ai.choose_card(hand, rows)
        self.assertEqual(chosen_card.number, 7)
        mock_random_choice.assert_called_once_with(hand.cards)

    def test_choose_row(self):
        rows = [
            Hand([Card(1), Card(3)]),
            Hand([Card(5)]),
            Hand([Card(7), Card(9)]),
            Hand([])
        ]
        card = Card(6)
        ai = AI()
        chosen_row = ai.choose_row(rows, card)
        self.assertEqual(chosen_row, 1)

    def test_choose_row_empty_hand(self):
        rows = [
            Hand([Card(1), Card(3)]),
            Hand([Card(5)]),
            Hand([Card(7), Card(9)]),
            Hand([])
        ]
        card = Card(10)
        ai = AI()
        chosen_row = ai.choose_row(rows, card)
        self.assertEqual(chosen_row, 3)

    def test_choose_row_no_valid_rows(self):
        rows = [
            Hand([Card(1), Card(3)]),
            Hand([Card(5)]),
            Hand([Card(7), Card(9)]),
            Hand([Card(8)])
        ]
        card = Card(10)
        ai = AI()
        chosen_row = ai.choose_row(rows, card)
        self.assertEqual(chosen_row, 0)

if __name__ == "__main__":
    unittest.main()
