# Convex Body Chasing

Exploratory project for implementing and evaluating online algorithms for the convex body chasing problem. The goal is to compare greedy follow-the-leader style methods with more competitive algorithms, generate adversarial sequences of convex bodies, and report empirical insights.

## Setup
- Requires Python 3.10+ and `pip`.
- Create a virtual environment (`python -m venv .venv && source .venv/bin/activate`).
- Install in editable mode: `pip install -e .`

## What’s here
- Minimal package scaffold in `src/convex_body_chasing` with a basic 2D ball body and a greedy follow-the-leader algorithm.
- Documentation plan lives in `docs/implementation-plan.md` (see after generation).
- Ready for expansion with additional body types, competitive algorithms, scenario generators, and Plotly-based evaluation plots.

## Quick demo
```python
import numpy as np
from convex_body_chasing.bodies import Ball2D
from convex_body_chasing.algorithms.greedy import follow_the_leader

bodies = [Ball2D(center=(i, 0.0), radius=1.0) for i in range(5)]
cost, points = follow_the_leader(bodies)
print(f"Movement cost: {cost:.2f}")
print("Visited points:", points)
```

## Next steps
- Implement richer convex body representations (polygons, intersections).
- Add competitive algorithms and adversarial scenario generators.
- Build evaluation notebooks and plots to compare cumulative costs and competitive ratios.
