from typing import List
from random import shuffle


class Card:
    def __init__(self, suit: str, num: str):
        self.__num: str = num
        self.__suit: str = suit

    def __str__(self):
        return self.__num + self.__suit


class Deck:
    """Deck of Cards, where each card has a number and  a suit"""
    count = 0

    def __init__(self, num: List[str], suits: List[str]):
        self.__cards: List[Card] = [Card(s, n) for s in suits for n in num]

    def __str__(self):
        return ' '.join(card.__str__() for card in self.__cards)

    def shuffle_deck(self):
        shuffle(self.__cards)
        Deck.count = 0

    def get_card(self, num: int) -> Card:
        card = self.__cards[num]
        return card

    def get_cards(self, num_of_cards: int) -> List[Card]:
        i = Deck.count
        Deck.count = i + num_of_cards
        return self.__cards[i: num_of_cards + i]


if __name__ == '__main__':
    suits = '♠ ♣ ♥ ♦'.split()
    numbers = '2 3 4 5'.split()
    deck = Deck(numbers, suits)
    deck.shuffle_deck()
    print(deck)
    listA = deck.get_cards(2)
    print([card.__str__() for card in listA])
    listB = deck.get_cards(4)
    print([card.__str__() for card in listB])
