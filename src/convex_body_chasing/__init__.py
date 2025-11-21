"""
Convex body chasing algorithms and utilities.

This package currently provides 2D convex bodies (ball, axis-aligned rectangle,
convex polygon, intersections) and a greedy follow-the-leader algorithm as a
starting point for further work.
"""

from .bodies import (
    AxisAlignedRectangle,
    Ball2D,
    ConvexBody,
    ConvexPolygon,
    Intersection,
    project_onto_intersection,
)

__all__ = [
    "AxisAlignedRectangle",
    "Ball2D",
    "ConvexBody",
    "ConvexPolygon",
    "Intersection",
    "project_onto_intersection",
]
