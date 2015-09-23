# MODELS
class Board(object):

    def __init__(self):
        # list of 7 columns, each with 6 slots
        column = []
        i = 0
        while i < 6:
            column.append(0)
            i += 1
        matrix = []
        j = 0
        while j < 7:
            matrix.append(column[:])
            j += 1
        self.status = matrix

    def get_status(self):
        return self.status

    def is_board_full(self, current_board):
        for column_index, column in enumerate(current_board):
            for space_index, space in enumerate(column):
                if space == 0:
                    return False
        return True
