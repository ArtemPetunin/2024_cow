import unittest
from row import Row
from card import Card

class TestRow(unittest.TestCase):
    def test_put_card(self):
        row = Row()
        row.put_card(Card(5))
        row.put_card(Card(3))
        row.put_card(Card(7))
        self.assertEqual([Card(3), Card(5), Card(7)], row.cards)

    def test_take_cards(self):
        row = Row()
        row.put_card(Card(5))
        row.put_card(Card(3))
        row.put_card(Card(7))
        taken_cards = row.take_cards()
        self.assertEqual([Card(3), Card(5), Card(7)], taken_cards)
        self.assertEqual([], row.cards)

    def test_save(self):
        row = Row()
        row.put_card(Card(5, 10))
        row.put_card(Card(3, 5))
        row.put_card(Card(7, 15))
        saved_data = row.save()
        self.assertEqual({"cards": [
            {"number": 3, "score": 5},
            {"number": 5, "score": 10},
            {"number": 7, "score": 15}
        ]}, saved_data)

    def test_load(self):
        saved_data = {
            "cards": [
                {"number": 3, "score": 5},
                {"number": 5, "score": 10},
                {"number": 7, "score": 15}
            ]
        }
        row = Row.load(saved_data)
        self.assertEqual([Card(3, 5), Card(5, 10), Card(7, 15)], row.cards)

if __name__ == "__main__":
    unittest.main()
