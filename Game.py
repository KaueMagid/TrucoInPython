from Deck import Deck, Card
import Players as pl
from typing import List

colors = dict(pink='\033[95m', blue='\033[94m', cyan='\033[96m', green='\033[92m',
              yelow='\033[93m', red='\033[91m', white='\033[0m', bold='\033[1m', under='\033[4m')

match: bool = True
order_numbers = 'Q J K A 2 3'
order_suits = '♦ ♠ ♥ ♣'
deck: Deck = Deck('Q J K A 2 3'.split(), '♠ ♣ ♥ ♦'.split())
teams: List[pl.Team] = []
players: List[pl.Player] = []


def set_number_of_players() -> int:
    while True:
        try:
            number: int = int(input(colors['white']+"Enter the number of players (2, 4 or 6): "))
            if number not in [2, 4, 6]:
                print(colors['red']+'invalid number')
            else:
                return number
        except ValueError:
            print(colors['red']+"Can't convert this str in int")


def set_players(num_of_players: int):
    for num in range(num_of_players):
        players.append(pl.Player(input(f'Player{num+1} Name: ')))


def set_teams(players: List[pl.Player]):
    while True:
        teams.clear()
        try:
            aux = input(colors['white'] + 'Which members of team A: ').split()
            if len(aux) == len(players)/2:
                teamA = []
                teamB = players

                for a in aux:
                    teamA.append(pl.search_player(a, players))
                    teamB.remove(pl.search_player(a, players))
                if len(teamA) != len(teamB):
                    raise ValueError("Teams do not have the same number of players")

                teams.append(pl.Team(teamA))
                teams.append(pl.Team(teamB))

                print(teams[0].__str__())
                if input('Reverse? ') == 'y':
                    teams[0].reverse()
                    pass

                print(teams[1].__str__())
                if input('Reverse? ') == 'y':
                    teams[1].reverse()
                    pass

                return None
        except ValueError:
            print(colors['red']+'Teams do not have the same number of players')


def turn():
    pass


if __name__ == '__main__':
    set_players(set_number_of_players())
    set_teams(players)
    while match:
        pass
