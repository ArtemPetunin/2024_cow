class Card:
    MAX_NUMBER = 100

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def score(self):
        return self.number

    def save(self):
        return {"number": self.number}

    @classmethod
    def load(cls, data):
        return cls(data["number"])
