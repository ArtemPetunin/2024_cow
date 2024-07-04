import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_init(self):
        card = Card(10)
        self.assertEqual(card.number, 10)

    def test_str(self):
        card = Card(42)
        self.assertEqual(str(card), "42")

    def test_score(self):
        card = Card(15)
        self.assertEqual(card.score(), 15)

    def test_save(self):
        card = Card(7)
        saved_data = card.save()
        self.assertEqual(saved_data, {"number": 7})

    def test_load(self):
        card = Card.load({"number": 25})
        self.assertEqual(card.number, 25)

    def test_max_number(self):
        self.assertEqual(Card.MAX_NUMBER, 100)

if __name__ == "__main__":
    unittest.main()
