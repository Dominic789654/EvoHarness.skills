# Version Control And Rollback

Use this when setting up EvoHarness state, selecting the active frontier, or visualizing progress.

## Version Policy

- Give every candidate a stable version identity: file name, import path, git commit, run directory, and iteration number.
- Record the parent version or baseline the candidate copied from.
- Preserve failed candidates. They are negative evidence for later diagnosis.
- Do not let a worse candidate replace the active frontier.
- Roll forward from the best known version after a regression, not from the latest version by default.

## Recommended Metadata

Add these fields to each `evolution_summary.jsonl` row when available:

```json
{
  "iteration": 3,
  "version": "v003_contrastive_memory",
  "parent": "v002_label_coverage",
  "system": "contrastive_memory",
  "avg_val": 48.2,
  "best_so_far": 48.2,
  "selected": true,
  "commit": "abc1234",
  "run_dir": "logs/run_003",
  "hypothesis": "Contrastive near-miss retrieval reduces adjacent-label confusion."
}
```

If `best_so_far` is missing, compute it as the cumulative max of the score column.

## Rollback Rules

- If a candidate regresses on the primary metric, keep its logs and report but keep the frontier pointer unchanged.
- If a candidate improves the primary metric but violates a hard constraint, reject it and keep the frontier pointer unchanged.
- If a candidate improves the primary metric with an unacceptable secondary metric cost, mark it as Pareto-only or rejected according to the project policy.
- If evaluation is noisy, require replication or confidence intervals before replacing the frontier.

## Visualization

Plot:

- x-axis: iteration or version index
- y-axis: eval score
- candidate score: raw score per evaluated version
- best-so-far score: cumulative frontier score

The expected healthy shape is not monotonic candidate scores. It is a mostly non-decreasing best-so-far frontier with failed experiments visible below it.

Use `scripts/plot_scores.py` for standard JSONL summaries.
