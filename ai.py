class AI(PlayerInteractions):
    def choose_card(self, hand, rows):
        if not hand.cards:
            return None
        return random.choice(hand.cards)

    def choose_row(self, rows, card):
        min_diff = float('inf')
        min_row = None
        for i, row in enumerate(rows):
            if not row.cards or card.number > row.cards[-1].number:
                diff = card.number - (row.cards[-1].number if row.cards else 0)
                if diff < min_diff:
                    min_diff = diff
                    min_row = i
        return min_row if min_row is not None else 0
