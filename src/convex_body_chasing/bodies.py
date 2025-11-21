from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Sequence, Tuple

import numpy as np

# Small numerical tolerance for containment checks and convergence.
DEFAULT_TOL = 1e-9


def _to_point(point: Iterable[float], *, dim: int) -> np.ndarray:
    """Convert an iterable to a float numpy array and validate dimension."""
    arr = np.asarray(point, dtype=float)
    if arr.shape != (dim,):
        raise ValueError(f"Expected point of shape ({dim},), got {arr.shape}.")
    return arr

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


@dataclass(frozen=True)
class AxisAlignedRectangle(ConvexBody):
    """Closed axis-aligned rectangle in R^2."""

    min_corner: Tuple[float, float]
    max_corner: Tuple[float, float]

    def __post_init__(self) -> None:
        lower = _to_point(self.min_corner, dim=2)
        upper = _to_point(self.max_corner, dim=2)
        if np.any(upper <= lower):
            raise ValueError("Max corner must be strictly greater than min corner in each dimension.")

    def contains(self, point: np.ndarray) -> bool:  # type: ignore[override]
        pt = _to_point(point, dim=2)
        lower = _to_point(self.min_corner, dim=2)
        upper = _to_point(self.max_corner, dim=2)
        return bool(np.all(pt >= lower - DEFAULT_TOL) and np.all(pt <= upper + DEFAULT_TOL))

    def closest_point(self, previous_point: np.ndarray) -> np.ndarray:  # type: ignore[override]
        pt = _to_point(previous_point, dim=2)
        lower = _to_point(self.min_corner, dim=2)
        upper = _to_point(self.max_corner, dim=2)
        return np.clip(pt, lower, upper)
