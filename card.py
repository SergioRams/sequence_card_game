class Card:
    """
    Card class, used to build a card deck.
    """

    SYMBOLS = ('hearts', 'clubs', 'spades', 'diamonds')
    FACE_VALUE = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11,
                  'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, symbol, value):
        # Clubs, Hearts, Spades, Diamonds
        self.symbol = symbol
        # Numeric value
        self.value = value

    @property
    def value(self):
        return self._value

    @property
    def symbol(self):
        return self._symbol

    @value.setter
    def value(self, v):
        if str(v) not in self.FACE_VALUE:
            raise Exception('not a valid card value')
        else:
            self._value = {str(v): self.FACE_VALUE[str(v)]}

    @symbol.setter
    def symbol(self, s):
        if s not in self.SYMBOLS:
            raise Exception('not a valid card symbol')
        else:
            self._symbol = s

    def get_card_details(self):
        return self.symbol, self.value
