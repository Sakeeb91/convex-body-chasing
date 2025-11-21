import unittest

import numpy as np

from convex_body_chasing.bodies import AxisAlignedRectangle


class AxisAlignedRectangleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rect = AxisAlignedRectangle(min_corner=(0.0, 0.0), max_corner=(2.0, 1.0))

    def test_contains_interior_and_boundary(self) -> None:
        self.assertTrue(self.rect.contains(np.array([1.0, 0.5])))
        self.assertTrue(self.rect.contains(np.array([0.0, 1.0])))
        self.assertFalse(self.rect.contains(np.array([2.1, 0.5])))

    def test_projection_clips_to_edges(self) -> None:
        projected = self.rect.closest_point(np.array([3.0, -1.0]))
        np.testing.assert_allclose(projected, np.array([2.0, 0.0]))


if __name__ == "__main__":
    unittest.main()
