class Player:

    def __init__(self, name, team, score=0):
        self.name = name
        self.team = team
        self.score = score
        # list of cards
        self.hand = []

    def draw_hand(self, deck, num_cards):
        """
        Given a Deck object it then draws a hand from it.
        :param deck: Deck object
        :param num_cards: number of cards per hand
        """

        self.hand = deck.deal_cards(num_cards)

    def show_hand(self):
        """
        Prints current player hand
        """

        print(f"{self.name.title()}'s cards are:")
        for card in self.hand:
            print(card.get_card_details())

    def place_chip_randomly(self):
        """
        """
        pass
