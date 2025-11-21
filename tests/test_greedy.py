import unittest

import numpy as np

from convex_body_chasing.algorithms.greedy import follow_the_leader
from convex_body_chasing.bodies import Ball2D


class GreedyAlgorithmTests(unittest.TestCase):
    def test_follow_the_leader_on_linear_balls(self) -> None:
        bodies = [Ball2D(center=(i, 0.0), radius=1.0) for i in range(5)]
        cost, points = follow_the_leader(bodies, start=(0.0, 0.0))

        self.assertEqual(len(points), len(bodies) + 1)
        self.assertGreaterEqual(cost, 0.0)
        np.testing.assert_allclose(points[0], np.array([0.0, 0.0]))
        # Should end on the boundary of the final ball, x approximately 4 - 1
        self.assertAlmostEqual(points[-1][0], 3.0, places=6)
        self.assertAlmostEqual(points[-1][1], 0.0, places=6)


if __name__ == "__main__":
    unittest.main()
