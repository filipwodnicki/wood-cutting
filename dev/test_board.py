from unittest import TestCase

from dev.board import Board


class TestBoard(TestCase):

    #test "insert" Class method

    def test_insert_type(self): # assert type != string

        b = Board()

        self.assertRaises(Exception, b.insert, 'car')

    def test_insert_size(self): #assert can't insert something big. (max board size = 2050)

        b = Board()

        with self.assertRaises(Exception):
            b.insert(1000)
            b.insert(1000)
            b.insert(51)

        b2 = Board()

        self.assertRaises(Exception, b2.insert, 2051)

    def test_insert_space(self): # assert space remaining works as planned
        b = Board()

        b.insert(100)

        self.assertEqual(b.space_remaining, 1950)

        b.insert(850)

        self.assertEqual(b.space_remaining, 1100)

    # test "remove" Class method

    def test_remove(self):

        b = Board()
        b.insert(50)

        # assert can't remove something that doesn't exist
        self.assertRaises(Exception, b.remove, 100)
        # assert space remaining works correctly
        self.assertEquals(b.space_remaining, 2000)

        b.remove(50)

        # assert can't remove something that was recently removed
        self.assertRaises(Exception, b.remove, 50)
        # assert space remaining works correctly
        self.assertEquals(b.space_remaining, 2050)