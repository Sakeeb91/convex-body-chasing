from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Tuple

import numpy as np

ArrayLikePoint = Iterable[float]


class ConvexBody(ABC):
    """Abstract interface for convex bodies in R^d."""

    @abstractmethod
    def closest_point(self, previous_point: np.ndarray) -> np.ndarray:
        """Project the previous point onto the body."""

    @abstractmethod
    def contains(self, point: np.ndarray) -> bool:
        """Return True if the point lies inside the body."""


@dataclass(frozen=True)
class Ball2D(ConvexBody):
    """Closed Euclidean ball in R^2."""

    center: Tuple[float, float]
    radius: float

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError("Radius must be positive.")

    def _to_array(self, point: ArrayLikePoint) -> np.ndarray:
        arr = np.asarray(point, dtype=float)
        if arr.shape != (2,):
            raise ValueError("Expected a 2D point shaped (2,).")
        return arr

    def contains(self, point: np.ndarray) -> bool:  # type: ignore[override]
        point_arr = self._to_array(point)
        center_arr = self._to_array(self.center)
        return np.linalg.norm(point_arr - center_arr) <= self.radius + 1e-12

    def closest_point(self, previous_point: np.ndarray) -> np.ndarray:  # type: ignore[override]
        prev = self._to_array(previous_point)
        center_arr = self._to_array(self.center)
        direction = prev - center_arr
        distance = np.linalg.norm(direction)
        if distance <= self.radius:
            return prev
        if distance == 0:
            return center_arr + np.array([self.radius, 0.0])
        return center_arr + direction / distance * self.radius
