import random

class Card:
    """Клас для представлення карти"""
    suits = ['Черви', 'Бубни', 'Піки', 'Трефи']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return f"{self.rank} {self.suit}"


class Deck:
    """Клас для представлення колоди карт"""
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        self.shuffle_deck()

    def shuffle_deck(self):
        """Перемішати колоду"""
        random.shuffle(self._cards)

    def get_card_by_position(self, position):
        """Отримати карту за номером у колоді (нумерація з 0)"""
        if 0 <= position < len(self._cards):
            return str(self._cards[position])
        return "Некоректна позиція!"

    def get_all_cards(self):
        """Отримати всі карти у колоді"""
        return [str(card) for card in self._cards]

    def draw_card(self):
        """Видати одну карту з колоди"""
        if self._cards:
            return str(self._cards.pop(0))
        return "Усі карти роздані!"

    def draw_six_cards(self):
        """Видати 6 карт з колоди"""
        if len(self._cards) >= 6:
            return [str(self._cards.pop(0)) for _ in range(6)]
        return "У колоді недостатньо карт для видачі 6 штук!"



if __name__ == "__main__":

    deck = Deck()

    print("Перемішана колода карт:")
    print(deck.get_all_cards())

    print("\nКарта за позицією 5:")
    print(deck.get_card_by_position(5))

    print("\nВидати одну карту:")
    print(deck.draw_card())

    print("\nВидати 6 карт:")
    print(deck.draw_six_cards())

    print("\nКолода після видачі карт:")
    print(deck.get_all_cards())

    print("\nПовторне перемішування:")
    deck.shuffle_deck()
    print(deck.get_all_cards())
