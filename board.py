class Board:

    # sequence board is
    ROWS = 10
    COLS = 10

    def __init__(self):

        self.board = [
            # first row
            [('corner', 'corner', 'corner'), ('2', 'spades', 'empty'), ('3', 'spades', 'empty'), ('4', 'spades', 'empty'), ['5', 'spades', 'empty'],
             ('6', 'spades', 'empty'), ('7', 'spades', 'empty'), ('8', 'spades', 'empty'), ('9', 'spades', 'empty'), ('corner', 'corner', 'corner')],
            # second row
            [('6', 'clubs', 'empty'), ('5', 'clubs', 'empty'), ('4', 'clubs', 'empty'), ('3', 'clubs', 'empty'), ('2', 'clubs', 'empty'),
             ('ace', 'hearts', 'empty'), ('king', 'hearts', 'empty'), ('queen', 'hearts', 'empty'), ('10', 'hearts', 'empty'), ('10', 'spades', 'empty')],
            # third row
            [('7', 'clubs', 'empty'), ('ace', 'spades', 'empty'), ('2', 'diamonds', 'empty'), ('3', 'diamonds', 'empty'), ('4', 'diamonds', 'empty'),
             ('5', 'diamonds', 'empty'), ('6', 'diamonds', 'empty'), ('7', 'diamonds', 'empty'), ('9', 'hearts', 'empty'), ('queen', 'spades', 'empty')],
        ]

    def print_board(self):
        """
        Prints current board status.
        """

        for row in range(3):
            for col in range(self.COLS):
                print(self.board[row][col])

    def get_cell_status(self, coords):
        """
        :param coords: coordinates tuple
        :return: returns cell status: 'empty' | 'team's color'
        """
        row, col = coords

        return self.board[row][col][2]

    def place_chip(self, coords):
        """
        Receives a player, that player belongs to a team, it then changes the status of the coordinates to the player's
        team.
        :param coords: coordinates tuple
        :return:
        """
        row, col = coords

        # checks that the coordinates are not a corner
        if self.board[row][col] != 'corner':
            if self.get_cell_status(coords) == 'empty':
                self.board[row][col][2] = 'player1'

    def check_sequence(self, team):
        """
        Checks if there is a sequence for the given team.
        :param team: team's color
        :return: tuple(boolean, team)
        """
        pass
