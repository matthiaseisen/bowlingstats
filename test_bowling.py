import unittest
from bowling import Game


class TestBowling(unittest.TestCase):

    def setUp(self):
        pass

    def test_score(self):
        g1 = Game([(0, 0)] * 9 + [(0, 0, 0)])
        self.assertEqual(g1.score(), 0)
        g2 = Game([(0, 0)] * 10)
        self.assertEqual(g2.score(), 0)
        g3 = Game([(10, 0)] * 9 + [(10, 10, 10)])
        self.assertEqual(g3.score(), 300)
        g4 = Game([(10, 0)] * 9 + [(10, 0, 10)])
        self.assertEqual(g4.score(), 280)
        g5 = Game([(10, 0)] * 10)
        self.assertEqual(g5.score(), 270)
        g6 = Game(
            [
                (5, 3), (2, 7), (5, 2), (4, 6),
                (3, 5), (7, 2), (5, 3), (2, 0),
                (3, 0), (9, 1, 6)
            ]
        )
        self.assertEqual(g6.score(), 83)

    def test_valid_frames(self):
        g1 = Game([(0, 0)] * 10)
        self.assertTrue(g1.valid_frames())
        g2 = Game([(0, 0)] * 8 + [(0, 0, 0)])
        self.assertFalse(g2.valid_frames())
        g3 = Game([(0, 0)] * 10 + [(0, 0, 0)])
        self.assertFalse(g3.valid_frames())
        g4 = Game([(0, 0, 0)] + [(0, 0)] * 9)
        self.assertFalse(g4.valid_frames())
        g5 = Game([(0, 0)] * 9 + [(0, 0, 1)])
        self.assertFalse(g5.valid_frames())
        g6 = Game([(0, -1)] * 10)
        self.assertFalse(g6.valid_frames())
        g7 = Game([(0, 11)] * 10)
        self.assertFalse(g7.valid_frames())
        g8 = Game([(0, 'a')] * 10)
        self.assertFalse(g8.valid_frames())

    def test_partial_scores(self):
        g1 = Game([(10, 0)] * 9 + [(10, 10, 10)])
        self.assertEqual(
            g1.partial_scores(),
            [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
        )

if __name__ == '__main__':
    unittest.main()
