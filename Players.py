from Deck import Card
from typing import List


class Player:
    cont = 1

    def __init__(self, name: str = 'Player'):
        if name == 'Player':
            name = name + str(Player.cont)
            Player.cont += 1

        self.__name: str = name
        self.__deck: List[Card] = []

    def __str__(self):
        return self.__name

    def set_deck(self, cards: List[Card]):
        self.__deck = cards

    def print_deck(self):
        print([card.__str__() for card in self.__deck])

    def play_card(self, num_card: int) -> Card:
        card = self.__deck[num_card]
        self.__deck.remove(card)
        return card


class Team:

    def __init__(self, teammate: List[Player]):
        self.__teammate = teammate
        self.__points: int = 0

    def __str__(self):
        return ' '.join(player.__str__() for player in self.__teammate)

    def increment_points(self, points: int):
        self.__points += points

    def reverse(self):
        self.__teammate = reversed(self.__teammate)

def search_player(name: str, players: List[Player]):
    p: Player
    for p in players:
        if name == p.__str__():
            return p


if __name__ == '__main__':
    from Deck import Deck
    p1 = Player()
    p2 = Player()
    p3 = Player()
    p4 = Player()
    T1 = Team([p1, p2])
    T2 = Team([p3, p4])
    deck = Deck('Q J K A 2 3'.split(), '♠ ♣ ♥ ♦'.split())
    deck.shuffle_deck()
    print(T1)
    print(T2)
    p1.set_deck(deck.get_cards(3))
    p2.set_deck(deck.get_cards(3))
    p3.set_deck(deck.get_cards(3))
    p4.set_deck(deck.get_cards(3))
    p1.print_deck()
    p2.print_deck()
    p3.print_deck()
    p4.print_deck()
