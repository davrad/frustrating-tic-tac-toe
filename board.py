class Board():


    def __init__(self, field_optional=0):
        if field_optional:
            self.field = field_optional
        else:
            self.field = [['', '', ''], ['', '', ''], ['', '', '']]


    def check_board(self):
        """
        Returns player character if someone won, else False
        """
        valid, player = self.check_rows(self.field)
        if valid:
            return player
        valid, player = self.check_rows(self.transpose())    # Checks columns with transposed matrix
        if valid:
            return player
        valid, player = self.check_diagonals(self.field)
        if valid:
            return player

        return False

    def transpose(self):
        """
        Gets as an input, a two dimensional list and returns the transpose of it
        """
        return list(map(list, zip(*(self.field))))


    def check_rows(self, field):
        for row in field:
            if '' not in row and len(set(row)) == 1:
                return True, row[0]

        return False, ''


    def check_diagonals(self, field):
        diag = [field[i][i] for i in range(len(field))]
        if '' not in diag and len(set(diag)) == 1:          # Check main diagonal
            return True, diag[0]
        if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '':       # check diag from upper right to lower left
            return True, field[0][2]
        return False, ''


    def draw_field(self, field=None):

        board_copy = self.field[:] if not field else field

        # Collection of strings to print
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
        for row in self.field:
            if '' in row:
                return False
        return True


    def game_finished(self):
        """
        Returns True, if game results in draw, if someone wins the player character, else False
        """
        return self.check_board() or self.check_draw()
