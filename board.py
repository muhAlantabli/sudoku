"""Board Module
"""


class Board:
    """Class to represent gaming board."""

    def __init__(self):
        self._length = 9
        self._board = [[0 for _ in range(self._length)]
                       for i in range(self._length)]

    def __str__(self):
        for i in range(self._length):
            if i == 0:
                _str = '      ' + \
                    '   '.join((str(i)
                                for i in range(1, self._length + 1))) + '\n'
                _str += '    +' + '~~~~~~~~~~~+'*3 + '\n'
            elif i % 3 == 0:
                _str += '    +' + '~~~~~~~~~~~+'*3 + '\n'
            else:
                _str += '    +-----------------------------------+\n'

            for j in range(self._length):
                if j == 0:
                    _str += '  ' + str(i + 1) + ' | ' + \
                        str(self._board[i][j]) + ' '
                else:
                    _str += '| ' + str(self._board[i][j]) + ' '
            _str += '|\n'
        _str += '    +' + '~~~~~~~~~~~+'*3 + '\n'
        return _str

    def fill(self):
        """filling board with initial state for the game."""
        row = 0
        while row != self._length:
            line = input(' Row ' + str(row + 1) + ': ')
            if line:
                col = 0
                for number in list(line):
                    try:
                        value = int(number)
                    except ValueError:
                        print('Only integers between 0-9, try again!')
                        while True:
                            cell_value = input(f'  Cell({row+1}, {col+1}) : ')
                            if not (cell_value.isdecimal() and int(cell_value)):
                                print('Wrong again!')
                                continue
                            value = int(cell_value)
                            break
                    if value:
                        self._board[row][col] = value
                    col += 1
            row += 1
