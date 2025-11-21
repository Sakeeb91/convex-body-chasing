"""
Convex body chasing algorithms and utilities.

This package currently provides a minimal 2D ball representation and
a greedy follow-the-leader algorithm as a starting point for further work.
"""

from .bodies import Ball2D, ConvexBody

__all__ = ["Ball2D", "ConvexBody"]
