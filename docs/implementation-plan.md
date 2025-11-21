# Implementation Plan: Convex Body Chasing Algorithms

## Goals and Scope
- Build a modular Python toolkit for online convex body chasing in 2D/low-d dimensions.
- Compare greedy follow-the-leader (FTL) baselines with classical competitive algorithms and stress-test via adversarial scenarios.
- Provide reproducible experiments (metrics, plots) and a clear path to extend with LLM-assisted algorithm ideation.

## Architecture and Stack
- Language: Python 3.10+.
- Core libs: `numpy` (vector math), `matplotlib` (visualization), optional `shapely` for polygon ops (guard with extras).
- Layout: `src/convex_body_chasing` package with submodules:
  - `bodies/`: convex sets (balls, ellipses, half-spaces, intersections, polygons).
  - `algorithms/`: online strategies (FTL/metric projection, competitive algorithms, randomized variants).
  - `scenarios/`: generators for random walks, drifting centers, nested/adversarial sequences.
  - `evaluation/`: simulation harness, metrics (cumulative cost, competitive ratio estimates), plotting utilities.
  - `llm/` (optional): prompts/tools to auto-generate adversarial sequences or code suggestions; keep behind feature flag.
- Testing: `unittest`/`pytest` + property tests for geometric invariants; small golden fixtures for scenarios.

## Milestones and Workstreams
1) **Geometry Primitives**
   - Implement `ConvexBody` protocol with `closest_point` projection and `contains`.
   - Bodies: `Ball2D`, axis-aligned rectangle, convex polygon (supporting intersection of half-spaces), generic intersection wrapper.
   - Utilities: distance, movement cost, random body samplers; ensure numerical robustness (eps tolerances).

2) **Algorithms**
   - Baseline: FTL via projection (already scaffolded).
   - Competitive candidates: (a) move-to-centroid with step size cap, (b) mirror-descent-inspired update with regularization, (c) nested Steiner point or barycentric update for polygons, (d) “move to nearest feasible point” (Euclidean projection) as strawman.
   - Randomized variants: add small Gaussian perturbations or randomized tie-breaking for adversarial resilience.
   - Interface: `Algorithm.run(bodies, start)` returning cost trace, points, and per-step metadata (step cost, body id).

3) **Scenario Generation**
   - Random walks/drift: centers follow AR(1) or Gaussian drift; radii vary slowly.
   - Adversarial: nested shrinking sets, alternating half-spaces causing zig-zags, sequences from literature demonstrating high FTL cost.
   - Realistic: capacity-style changes (e.g., boxes moving along a corridor) to illustrate applied behavior.
   - Make reproducible via seeds; support JSON/YAML configs for batches.

4) **Evaluation Pipeline**
   - Simulation runner that accepts algorithm + scenario config, emits `RunResult(cost, points, per_step)`.
   - Metrics: cumulative cost over time, per-step displacement, empirical competitive ratio vs. offline optimum (approx via convex program for small horizons).
   - Visualization: trajectories, body overlays, cost vs. timestep plots; optional animation/gif export.
   - Reporting: notebook/template summarizing wins/failure modes with saved figures.

5) **LLM Collaboration (Optional)**
   - Prompt templates for “propose adversarial sequence” and “suggest algorithm tweak”.
   - Sandbox execution: keep generated code under `llm/` drafts, gated via flag to avoid unreviewed execution.

6) **Quality and DX**
   - Type hints + lint (`ruff`) and format (`black`) gates.
   - CI: lint + tests + example run on a short scenario.
   - Docs: README quickstart, short HOWTO for adding a new algorithm/body, and issue templates.

## Deliverables by Checkpoint
- **CP1 (Geometry)**: Bodies implemented with tests; projection correctness for representative points.
- **CP2 (Algorithms)**: FTL + at least 2 competitive/randomized variants with unit tests and small scenario smoke tests.
- **CP3 (Scenarios & Eval)**: Scenario generators + runner producing metrics/plots for a small batch; example notebook with two plots.
- **CP4 (Reporting & LLM optional)**: Written summary of behavior, optional LLM module with guardrails, CI green.

## Initial Task Cut (issues will mirror)
- Flesh out `ConvexBody` derivatives (ball, rectangle, polygon) with projection helpers.
- Implement algorithm interface + FTL + one competitive algorithm.
- Build scenario generator API and a few canned scenarios.
- Add evaluation runner and plotting utilities with CLI/notebook entry point.
- Baseline tests for geometry and algorithms; simple CI workflow.
