import unittest

import numpy as np

from convex_body_chasing.bodies import ConvexPolygon


class ConvexPolygonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.square = ConvexPolygon(
            vertices=[(0.0, 0.0), (2.0, 0.0), (2.0, 1.0), (0.0, 1.0)]
        )

    def test_contains(self) -> None:
        self.assertTrue(self.square.contains(np.array([1.0, 0.5])))
        self.assertTrue(self.square.contains(np.array([2.0, 0.5])))
        self.assertFalse(self.square.contains(np.array([3.0, 0.5])))

    def test_projection_to_edge(self) -> None:
        projected = self.square.closest_point(np.array([3.0, 0.5]))
        np.testing.assert_allclose(projected, np.array([2.0, 0.5]))

        projected2 = self.square.closest_point(np.array([1.0, -1.0]))
        np.testing.assert_allclose(projected2, np.array([1.0, 0.0]))


if __name__ == "__main__":
    unittest.main()
