
import unittest
from entities.rect import Rect


class TestRect(unittest.TestCase):
    """Tests for Rect entity

    """

    def setup(self):
        self.test_rect = Rect(0, 1, 2, 3)

    def test_rect_creation(self):
        self.test_rect = Rect(0, 1, 2, 3)

        self.assertEqual((0, 1, 2, 3), (self.test_rect.x,
                         self.test_rect.y, self.test_rect.x2, self.test_rect.y2))

        # self.assertIsNone(self.test_rect.child_right)
        # self.assertIsNone(self.test_rect.child_left)

    def test_rect_children(self):
        self.test_rect = Rect(0, 1, 2, 3)

        child1 = Rect(1, 1, 3, 3)
        child2 = Rect(2, 2, 4, 4)
        self.test_rect.child_right = child1
        self.test_rect.child_left = child2
        self.assertEqual(1, self.test_rect.child_right.x)
        self.assertEqual(2, self.test_rect.child_left.x)
