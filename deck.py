from card import Card
import random


class Deck:

    # total number of cards in a deck
    TOTAL_CARDS = 52
    # total number of cards in each suit
    SUIT = 13
    # possible card symbols
    SYMBOLS = ('hearts', 'clubs', 'spades', 'diamonds')
    # possible card values
    FACE_VALUE = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11,
                  'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, shuffle=True):
        """
        Creates an ordered deck.
        :param shuffle: shuffles deck order, default is True
        """

        # list of tuples: (symbol, {string_value, int_value})
        self.deck = []

        for symbol in self.SYMBOLS:
            for value in self.FACE_VALUE:
                self.deck.append(Card(symbol=symbol, value=value))

        if shuffle:
            self.shuffle_deck()

    def shuffle_deck(self):
        """
        Using random shuffle to mix up the deck order.
        """

        random.shuffle(self.deck)

    def print_deck(self):
        """
        Prints remaining cards from the deck.
        """

        for card in self.deck:
            print(card.get_card_details())

    def draw_card(self, show_card=False):
        """
        Checks if there's are cards on the deck and returns the top card from it.
        :param show_card: it will print the drawn card
        :return: the top card object from the deck
        """

        if len(self.deck) > 0:
            top_card = self.deck.pop()
            if show_card:
                print(f'You draw: {top_card.get_card_details()}')
            return top_card
        else:
            raise Exception('Card deck is empty!')

    def deal_cards(self, num_cards=7):
        """
        Used to deal cards to players. by Default it returns 7 cards.
        :param num_cards: how many cards
        :return: a list of cards
        """

        deal_cards = []
        for _ in range(num_cards):
            deal_cards.append(self.draw_card())

        return deal_cards
