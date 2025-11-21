import unittest

import numpy as np

from convex_body_chasing.bodies import AxisAlignedRectangle, Ball2D, Intersection


class IntersectionTests(unittest.TestCase):
    def setUp(self) -> None:
        rect = AxisAlignedRectangle(min_corner=(-1.0, -1.0), max_corner=(2.0, 1.0))
        ball = Ball2D(center=(0.0, 0.0), radius=1.0)
        self.body = Intersection(bodies=[rect, ball])

    def test_contains(self) -> None:
        self.assertTrue(self.body.contains(np.array([0.5, 0.0])))
        self.assertFalse(self.body.contains(np.array([2.5, 0.0])))

    def test_alternating_projection_enters_intersection(self) -> None:
        projected = self.body.closest_point(np.array([2.0, 0.0]))
        # Should land on ball boundary and within rectangle.
        self.assertLessEqual(np.linalg.norm(projected - np.array([0.0, 0.0])), 1.0 + 1e-9)
        self.assertTrue(self.body.contains(projected))


if __name__ == "__main__":
    unittest.main()
