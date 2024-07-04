class Human(PlayerInteractions):
    def choose_card(self, hand, rows):
        print(f"Your hand: {hand}")
        while True:
            try:
                card_number = int(input("Choose a card to play: "))
                card = next((c for c in hand.cards if c.number == card_number), None)
                if card:
                    return card
                else:
                    print("Invalid card number. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_row(self, rows, card):
        print("Current rows:")
        for i, row in enumerate(rows):
            print(f"{i+1}. {', '.join(map(str, row.cards))}")
        while True:
            try:
                row_index = int(input(f"Choose a row to play {card} (1-4): "))
                if 1 <= row_index <= 4:
                    return row_index - 1
                else:
                    print("Invalid row number. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")