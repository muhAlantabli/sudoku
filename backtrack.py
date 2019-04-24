"""Functions for solving game using backtracking algorithm
"""

from time import time


class Backtrack:
    """Class to implement backtracking methodology.
    """

    def __init__(self, _list, length):
        self._list = _list
        self._length = length

    def check_row(self, value, row):
        """Check current row if contains given value.

        Args:
            value (integer): searched value
            row (integer): current row

        Returns:
            boolean: False if value is found, otherwise True
        """

        for col in range(self._length):
            if self._list[row][col] == value:
                return False
        return True

    def check_col(self, value, col):
        """Check current column if contains given value.

        Args:
            value (integer): searched value
            col (integer): current column

        Returns:
            boolean: False if value is found, otherwise True
        """

        for row in range(self._length):
            if self._list[row][col] == value:
                return False
        return True

    def check_box(self, value, row, col):
        """check current box if contains given value.

        Args:
            value (integer): searched value
            row (integer): starting row of box
            col (integer): starting column of box

        Returns:
            boolean: False if value if found, otherwise True
        """

        for i in range(row, row+3):
            for j in range(col, col+3):
                if self._list[i][j] == value:
                    return False
        return True

    def check_empty_cells(self, _params):
        """check list for the first empty cell.

        Args:
            _params (dictionary): list of parameters passed to method
            [row, col, box_row, box_col]

        Returns:
            Boolean: True if empty value found, otherwise False
        """

        for row in range(self._length):
            if row % 3 == 0:
                # Register first row for current box
                _params['box_row'] = row

            for col in range(self._length):
                if col % 3 == 0:
                    # Register first column for current box
                    _params['box_col'] = col

                # If empty value found. register row and column
                if not self._list[row][col]:
                    _params['row'] = row
                    _params['col'] = col
                    return True
        return False

    def run(self):
        """Starting point

        Returns:
            Boolean: True if solution is found, otherwise False
        """

        _params = {'row': 0, 'col': 0, 'box_row': 0, 'box_col': 0}
        # Recursion stop condition
        if not self.check_empty_cells(_params):
            return True

        for value in range(1, 10):
            if self.check_row(value, _params['row']) and self.check_col(value, _params['col']) and self.check_box(value, _params['box_row'], _params['box_col']):
                self._list[_params['row']][_params['col']] = value

                if self.run():
                    return True
            self._list[_params['row']][_params['col']] = 0
        return False
