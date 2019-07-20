class Board:

    def __init__(self, field_optional=False):
        self.field = field_optional if field_optional else [['', '', ''], ['', '', ''], ['', '', '']]

    def check_board(self):
        """
        Returns player character if someone won, else False
        """
        valid, player = self.check_rows(self.field)
        if valid:
            return player
        valid, player = self.check_rows(self.transpose())
        if valid:
            return player
        valid, player = self.check_diagonals(self.field)
        if valid:
            return player
        return False

    def transpose(self):
        """
        Gets a symmetrical two dimensional matrix/ list as an input, and returns the transpose
        """
        return list(map(list, zip(*(self.field))))

    def check_rows(self, field):
        for row in field:
            if '' not in row and len(set(row)) == 1:
                return True, row[0]

        return False, ''

    def check_diagonals(self, field):
        diag = [field[i][i] for i in range(len(field))]
        # Check main diagonal
        if '' not in diag and len(set(diag)) == 1:
            return True, diag[0]
        # check diag from upper right to lower left
        if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '':
            return True, field[0][2]
        return False, ''

    def draw_field(self, field=None):

        board_copy = self.field[:] if not field else field

        seperator = "-------+-------+-------"
        in_between = "       |       |       "
        values = "   {0}   |   {1}   |   {2}   "

        for i in range(11):
            if (i % 4) == 3:
                print(seperator)
            elif (i % 2) == 0:
                print(in_between)
            else:
                row = [" " if x == '' else x for x in board_copy[0]]
                print(values.format(row[0], row[1], row[2]))
                board_copy.pop(0)

    def check_valid_move(self, pos):
        if pos < 0 or pos > 8:
            return False
        return self.field[pos // 3][pos % 3] == ''

    def update_board(self, pos, char):
        self.field[pos // 3][pos % 3] = char

    def check_draw(self):
        return not list(filter(lambda row: '' in row, self.field))

    def game_finished(self):
        """
        Returns True, if game results in draw, if someone wins the player character, else False
        """
        return self.check_board() or self.check_draw()
