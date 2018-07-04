from unittest import TestCase

from dev.woodcut import Board


class TestBoard(TestCase):

    def test_insert_type(self):

        b = Board()

        self.assertRaises(Exception, b.insert, 'car')

    def test_insert_size(self):

        b = Board()

        with self.assertRaises(Exception):
            b.insert(1000)
            b.insert(1000)
            b.insert(51)

        b2 = Board()

        self.assertRaises(Exception, b2.insert, 2051)

    def test_insert_space(self):
        b = Board()

        b.insert(100)

        self.assertEqual(b.space_remaining, 1950)

        b.insert(850)

        self.assertEqual(b.space_remaining, 1100)

    def test_remove(self):

        b = Board()
        b.insert(50)

        self.assertRaises(Exception, b.remove, 100)
        self.assertEquals(b.space_remaining, 2000)

        b.remove(50)

        self.assertRaises(Exception, b.remove, 50)
        self.assertEquals(b.space_remaining, 2050)