# Advanced Exploration & Real-World Directions

## Advanced Algorithmic Ideas
- **Steiner-point / centroidal schemes**: Implement Steiner-point moves for polygons/half-spaces; compare to FTL on adversarial nests.
- **Mirror/proximal descent**: Add mirror-descent updates with entropy/Euclidean regularizers; tune step sizes to trade stability vs. agility.
- **Randomized defenses**: Inject small noise or randomized tie-breaks to mitigate adversarial sequences; measure variance and worst-case bounds.
- **Hybrid offline-online**: Compute short-horizon offline optima (small convex programs) and warm-start online updates; compare to pure online baselines.
- **Higher dimensions**: Extend to d>2 with generic convex sets (half-space intersections) and stress-test computational cost.

## Scenario & Benchmark Extensions
- **Adversarial generators**: Automated nested/shrinking sets, alternating half-spaces, and zig-zag corridors; produce difficulty scores.
- **Structured drifts**: AR(1) or sinusoids for centers/radii; mixed noise + trend to probe tracking vs. chattering.
- **Replayable suites**: Versioned scenario configs (YAML/JSON) with seeds; publish a small benchmark table with expected cost ranges.

## Evaluation & Visualization
- **Metric suite**: Cumulative cost, per-step displacement, empirical competitive ratio vs. short-horizon optimum, stability (mean absolute jerk).
- **Plotly dashboards**: Interactive trajectories, body overlays, cost curves, and side-by-side algorithm comparisons; export static PNG + HTML.
- **Profiling**: Time/space profiling per algorithm; flag any O(n*d^3) hotspots when bodies grow complex.

## Real-World Touchpoints
- **Resource allocation with shifting constraints**: Model capacity/feasibility regions over time (e.g., datacenter quotas, logistics corridors).
- **Adaptive setpoints in control**: Online feasible set changes for robotic navigation or tracking under obstacle growth/shrink.
- **Portfolio/asset bounds**: Moving convex polytopes representing risk/return constraints; compare online moves to transaction cost proxies.
- **Scheduling with evolving windows**: Time-window intersections as convex bodies; analyze travel/move cost analogs.

## Tooling & DX
- **LLM-assisted adversaries**: Prompt an LLM to propose hard scenarios or code sketches, store under `llm/` with manual review gates.
- **CLI/notebooks**: Provide `scripts/run_sim.py` and a notebook to reproduce benchmark plots with a single command.
- **CI gates**: Add lint/format (ruff/black), deterministic scenario smoke tests, and HTML figure artifacts for PRs.
