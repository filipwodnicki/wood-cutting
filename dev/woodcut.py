boardCollection = []

pieces = [450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261]


class Board(object):
    board_length = 2050.

    def __init__(self):
        self.contents = []
        self.space_remaining = self.board_length

    def insert(self, piece_length):

        if self.space_remaining >= piece_length:

            self.contents.append(piece_length)
            self.space_remaining -= piece_length

        else:
            raise Exception('piece of length too long to be inserted')

    def remove(self, piece_length):

        if piece_length in self.contents:

            self.contents.remove(piece_length)
            self.space_remaining += piece_length

        else:
            raise Exception('piece not on the Board!')


# Algorithm

boardCollection.append(Board())

pieces.sort(reverse=True)  # sort in ascending order


def try_placing(piece):
    for board in boardCollection:
        if board.space_remaining >= piece:
            board.insert(piece)
            pieces.remove(piece)
            return True
    return False


for piece in pieces[:]:

    #     print ( boardCollection[0].contents )

    if try_placing(piece) == True:
        pass
    else:
        boardCollection.append(Board())
        boardCollection[-1].insert(piece)
        pieces.remove(piece)