#!/usr/bin/env python3
"""Plot EvoHarness version score trends from evolution_summary.jsonl."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _load_rows(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return rows


def _score(row: dict, field: str) -> float | None:
    value = row.get(field)
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _label(row: dict, index: int) -> str:
    return str(
        row.get("version")
        or row.get("system")
        or row.get("name")
        or row.get("candidate")
        or index
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Plot candidate score and best-so-far frontier over versions."
    )
    parser.add_argument("summary", type=Path, help="Path to evolution_summary.jsonl")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("plots/version_scores.png"),
        help="Output image path (default: plots/version_scores.png)",
    )
    parser.add_argument(
        "--score-field",
        default="avg_val",
        help="Score field to plot (default: avg_val)",
    )
    parser.add_argument(
        "--title",
        default="Harness Evolution Score",
        help="Plot title",
    )
    args = parser.parse_args()

    rows = _load_rows(args.summary)
    points = []
    for idx, row in enumerate(rows, 1):
        score = _score(row, args.score_field)
        if score is None:
            continue
        points.append((idx, _label(row, idx), score))

    if not points:
        raise SystemExit(f"No numeric '{args.score_field}' values found in {args.summary}")

    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise SystemExit("matplotlib is required: python -m pip install matplotlib") from exc

    xs = [p[0] for p in points]
    labels = [p[1] for p in points]
    scores = [p[2] for p in points]
    best = []
    current = float("-inf")
    for score in scores:
        current = max(current, score)
        best.append(current)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    plt.plot(xs, scores, marker="o", linewidth=1.5, label="candidate score")
    plt.plot(xs, best, marker="o", linewidth=2.5, label="best so far")
    plt.title(args.title)
    plt.xlabel("version")
    plt.ylabel(args.score_field)
    plt.grid(True, alpha=0.3)
    plt.legend()

    if len(points) <= 30:
        plt.xticks(xs, labels, rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig(args.output, dpi=160)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
