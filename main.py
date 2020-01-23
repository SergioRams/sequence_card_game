from player import Player
from board import Board
from deck import Deck


def main():
    """
    Game
    """

    # GAME SET UP
    HAND_SIZE = 7
    # create game board
    game_board = Board()
    # create and shuffle a Deck
    deck = Deck(shuffle=True)
    # create 2 players (TODO : make a factory for this step, we don't know how many players will be there until runtime)
    players = [Player('Mike', 'Red'), Player('Gabriela', 'Blue')]

    # draw player's hands
    [player.draw_hand(deck, num_cards=HAND_SIZE) for player in players]

    # show current cards
    [player.show_hand() for player in players]


if __name__ == "__main__":
    main()
