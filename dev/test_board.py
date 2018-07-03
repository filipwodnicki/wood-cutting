from unittest import TestCase

from dev.woodcut import Board


class TestBoard(TestCase):
    def test_insert(self):

        b = Board()

        self.assertRaises(Exception, b.insert, 'car')

    # def test_remove(self):
    #     self.fail()
