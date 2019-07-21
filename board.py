class Board:

    def __init__(self, field_optional=False):
        self.field = field_optional if field_optional else [['', '', ''], ['', '', ''], ['', '', '']]

    def check_board(self) -> str:
        """Checks field if there is a winner"""
        player = self.check_rows(self.field) or self.check_rows(self.transpose()) or self.check_diagonals()
        return player

    def transpose(self) -> list:
        """Returns transpose of the field for column checking"""
        return list(map(list, zip(*self.field)))

    def check_rows(self, field: list) -> str:
        """Checks the field if a row is occupied with the same char"""
        for row in field:
            if '' not in row and len(set(row)) == 1:
                return row[0]
        return ''

    def check_diagonals(self) -> str:
        """Checks both diagonals of the field if either one of them contain the same character"""
        diag = [self.field[i][i] for i in range(len(self.field))]
        if '' not in diag and len(set(diag)) == 1:
            return diag[0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != '':
            return self.field[0][2]
        return ''

    def draw_field(self, field=None):
        """Prints out a representation of the field to the terminal"""
        board_copy = self.field[:] if not field else field

        separator = "-------+-------+-------"
        between_sep = "       |       |       "
        values = "   {0}   |   {1}   |   {2}   "

        for i in range(11):
            if (i % 4) == 3:
                print(separator)
            elif (i % 2) == 0:
                print(between_sep)
            else:
                row = [" " if x == '' else x for x in board_copy[0]]
                print(values.format(row[0], row[1], row[2]))
                board_copy.pop(0)

    def check_valid_move(self, pos: int) -> bool:
        """Checks if move is out of bounds and field is not already occupied"""
        if pos < 0 or pos > 8:
            return False
        return self.field[pos // 3][pos % 3] == ''

    def update_board(self, pos, char):
        self.field[pos // 3][pos % 3] = char

    def check_draw(self) -> bool:
        """Checks if every box is occupied"""
        return not list(filter(lambda row: '' in row, self.field))

    def game_finished(self) -> bool:
        """Checks if either someone has won or the game ended in a draw"""
        return self.check_board() or self.check_draw()

    def get_winner(self) -> str:
        return self.check_board()
