class PlayerInteractions(ABC):
    @abstractmethod
    def choose_card(self, hand, rows):
        pass

    @abstractmethod
    def choose_row(self, rows, card):
        pass