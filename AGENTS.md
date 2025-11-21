# Repository Guidelines

## Project Structure & Module Organization
- Code lives in `src/convex_body_chasing/` with subpackages for `algorithms/` and geometry primitives (`bodies.py`).
- Tests are under `tests/`; add new tests alongside the module under test (e.g., `tests/test_algorithms_x.py`).
- Docs sit in `docs/`, including `implementation-plan.md`; update alongside feature work.

## Build, Test, and Development Commands
- Install (editable, global override currently used): `pip3 install --break-system-packages -e .`
- Run tests: `python3 -m unittest` (add new suites to `tests/`).
- Quick import demo (Python shell): `from convex_body_chasing.algorithms.greedy import follow_the_leader`

## Coding Style & Naming Conventions
- Python 3.10+, type hints everywhere; prefer `dataclass` for data carriers.
- Stick to concise, descriptive names (e.g., `RunResult`, `ScenarioConfig`).
- Formatting/linting: add `ruff`/`black` if introducing tooling; keep lines ~100 chars and use f-strings.
- Geometry: small eps tolerances for numeric comparisons; document any nontrivial projection logic.

## Testing Guidelines
- Use `unittest`; mirror module names (e.g., `test_bodies.py`, `test_greedy.py`).
- Cover geometry edge cases (boundary points, degenerate directions) and algorithm cost sanity checks.
- Keep tests deterministic; seed any randomness and assert expected movement costs or invariants.

## Commit & Pull Request Guidelines
- Commits: short present-tense summaries (examples: “Add rectangle body projection”, “Refine evaluation runner”).
- Link issues in PR descriptions (`Closes #N`), summarize behavior changes, and note test coverage.
- If adding visuals, attach Plotly HTML/PNG snapshots or describe the scenario used to generate them.

## Architecture Snapshot
- Core abstraction: `ConvexBody` with `closest_point` and `contains`.
- Algorithm surface: functions/classes returning `(cost, points, metadata)`; keep interfaces minimal and well-typed.
- Scenarios and evaluation should be config-driven and reproducible (seeded generators, saved metrics/plots).
