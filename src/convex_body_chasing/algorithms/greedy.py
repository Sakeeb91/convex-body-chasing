from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple

import numpy as np

from convex_body_chasing.bodies import ConvexBody

Point = np.ndarray


def follow_the_leader(
    bodies: Sequence[ConvexBody], start: Iterable[float] | None = None
) -> Tuple[float, List[Point]]:
    """
    Greedy online algorithm: move to the closest feasible point in the
    current convex body given the previous location.

    Returns cumulative movement cost and the visited points.
    """
    if not bodies:
        raise ValueError("At least one body is required.")

    current = (
        np.asarray(start, dtype=float)
        if start is not None
        else np.asarray(getattr(bodies[0], "center", np.zeros(2)), dtype=float)
    )
    points: List[Point] = [current]
    cost = 0.0

    for body in bodies:
        next_point = body.closest_point(current)
        step_cost = float(np.linalg.norm(next_point - current))
        cost += step_cost
        points.append(next_point)
        current = next_point

    return cost, points
