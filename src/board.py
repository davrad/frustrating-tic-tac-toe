class Board:
    """Class representing a tic tac toe board"""

    def __init__(self, field_optional=False) -> None:
        self.field = field_optional if field_optional else [['', '', ''], ['', '', ''], ['', '', '']]

    def check_board(self) -> str:
        """Checks field if there is a winner"""
        return self.check_rows(self.field) or self.check_rows(self.transpose()) or self.check_diagonals()

    def transpose(self) -> list:
        """Returns transpose of the field for column checking"""
        return list(map(list, zip(*self.field)))

    def check_rows(self, field: list) -> str:
        """Checks the field if a row is occupied with the same char"""
        finished_row = list(filter(lambda row: '' not in row and len(set(row)) == 1, field))
        return finished_row[0][0] if finished_row else ''

    def check_diagonals(self) -> str:
        """Checks both diagonals, of the field and if either one of them contain the same character"""
        diag = [self.field[i][i] for i in range(3)]
        mirror_diag = [self.field[0][2], self.field[1][1], self.field[2][0]]
        space_free = '' not in diag or '' not in mirror_diag
        the_same = len(set(diag)) == 1 or len(set(mirror_diag)) == 1
        return diag[1] if space_free and the_same else ''

    def check_valid_move(self, pos: int) -> bool:
        """Checks if move is out of bounds and field is not already occupied"""
        return (0 <= pos <= 8) and self.field[pos // 3][pos % 3] == ''

    def update_board(self, pos: int, char: str) -> None:
        """Inserts in the field at the given position the given char"""
        self.field[pos // 3][pos % 3] = char

    def check_draw(self) -> bool:
        """Checks if every box is occupied"""
        return not list(filter(lambda row: '' in row, self.field))

    def game_finished(self) -> bool:
        """Checks if either someone has won or the game ended in a draw"""
        return self.check_board() or self.check_draw()

    def get_winner(self) -> str:
        """Returns the winning character if a winner exists or '' in a draw"""
        return self.check_board()
