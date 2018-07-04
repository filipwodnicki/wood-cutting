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