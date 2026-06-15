---
name: evo-harness
description: "Use when Codex needs bounded auto-research for harness engineering: designing, running, or maintaining a Meta-Harness-style evolution loop over task-specific model harnesses such as memory systems, retrieval wrappers, prompt/context builders, tool-use scaffolds, or agent harness code. Trigger for requests to optimize a harness from traces, turn candidate history into hypotheses, define candidate interfaces, set up frontier/evolution logs, analyze candidate results, prevent search/test leakage, or register new candidate harnesses for benchmark evaluation."
---

# Evo Harness

## Purpose

Run bounded auto-research for harness engineering. Turn code, traces, metrics, and candidate history into falsifiable harness hypotheses, executable candidate code, and held-out evaluation discipline.

Optimize task-specific harness code around a fixed base model. Treat the harness as the editable layer that stores, retrieves, filters, formats, plans, or wraps tool use for a repeated task family.

Treat harness evolution as versioned research. Keep failed versions for analysis, but preserve a rollback path to the best earlier frontier when a new candidate regresses.

Do not present this as a way to rewrite a full production agent product or run open-ended scientific research. Use it for narrow, benchmarkable harness surfaces with clear interfaces and cheap-enough repeated evaluation.

## Readiness Check

Before proposing candidates, establish these fields. If a field is unavailable, mark it `unknown` and choose a conservative default.

- Fixed base model or model set
- Candidate harness interface
- Allowed code changes and out-of-scope changes
- Search split and held-out test split
- Primary metric and secondary metrics
- Baselines and strongest current harness
- Evaluation budget: candidates, wall time, tokens, cost, or trials
- Trace locations and result-file schema

If the domain is not yet specified, create a domain spec first. Use `references/domain-spec-template.md`.

## Hard Rules

- Keep held-out test traces, labels, and scores out of proposer context during search.
- Do not change the base model, tools, datasets, or evaluator unless the user explicitly changes the experiment.
- Do not hardcode dataset names, task IDs, benchmark answers, or hidden labels in candidate code.
- Prefer mechanism changes over parameter sweeps.
- Make each candidate test one falsifiable hypothesis.
- Preserve source code, scores, traces, and reports for later iterations.
- Validate imports and interface compliance before registering a candidate.
- Treat benchmark improvements as provisional until replicated or confirmed on held-out evaluation.
- Keep every evaluated version addressable by file name, commit, run directory, or manifest entry.
- Never overwrite the active frontier with a worse candidate; record regressions as research evidence and roll forward again from the best known version.

## Standard Files

Use the project's existing structure when present. Otherwise create the smallest compatible version:

- `agents/` or `harnesses/`: candidate source files
- `logs/`: search/validation traces
- `results/`: held-out test outputs
- `frontier_val.json`: current search frontier
- `evolution_summary.jsonl`: one JSON row per candidate
- `reports/`: short post-eval reports
- `pending_eval.json`: candidates for the outer evaluator
- `plots/`: version-vs-score charts when visualization is requested

Use `references/candidate-contracts.md` when defining the exact interface and output schema.
Use `references/version-control.md` when setting up candidate versioning, rollback, and score visualization.

## Research Loop

Treat each iteration as a bounded research cycle:

1. Observe: read source, metrics, frontier, and traces.
2. Diagnose: identify the failure mechanism.
3. Hypothesize: write a falsifiable mechanism-level claim.
4. Intervene: implement one candidate harness change.
5. Evaluate: run the agreed search metric.
6. Attribute: explain wins and regressions from trace evidence.
7. Select: keep the active frontier at the best validated version, not necessarily the newest version.
8. Preserve: write the result back to the experience store.

## Iteration Workflow

1. Read current state:
   - config and evaluator commands
   - baseline source files
   - `frontier_val.json`
   - `evolution_summary.jsonl`
   - recent success and failure traces

2. Diagnose failures:
   - identify recurring errors
   - compare successful and failed candidates
   - isolate whether failures come from retrieval, memory, prompt format, tool use, state mutation, latency, context limits, or evaluator mismatch

3. Write hypotheses:
   - state the mechanism
   - predict the metric direction
   - name the expected tradeoff, such as context length, cost, latency, or robustness

4. Prototype before full implementation:
   - use `/tmp` scripts or notebook-like snippets
   - test the core mechanism on real trace samples
   - compare at least one simple alternative when practical
   - delete scratch files when done

5. Implement candidates:
   - copy a proven baseline or frontier candidate
   - make targeted changes only
   - keep the public interface compatible
   - avoid unrelated cleanup

6. Validate:
   - run import checks
   - run interface or smoke tests
   - run the cheapest meaningful eval if available

7. Register:
   - write `pending_eval.json`
   - include name, file/import path, hypothesis, mechanism, base candidate, and expected tradeoff

8. After evaluation:
   - update frontier and summary files
   - keep regressed candidates in history, but set the active baseline/frontier to the best known version
   - write or update a short report using `references/iteration-report-template.md`
   - carry forward the trace-level lesson, not just the score

## Versioning And Visualization

Prefer normal git commits, candidate manifests, or immutable run directories to track versions. Record enough metadata to answer: which code produced this score, what was the parent version, and why was it kept or rejected?

When the user asks for progress visualization, generate a chart with version or iteration on the x-axis and eval score on the y-axis. Plot both candidate score and best-so-far frontier when available. Use `scripts/plot_scores.py` for `evolution_summary.jsonl` files.

## Candidate Quality Checklist

Reject or rewrite a candidate if:

- It only changes constants, thresholds, prompt adjectives, or retrieval counts.
- It changes multiple mechanisms at once without a reason.
- It depends on held-out examples or task-specific answers.
- It silently changes the evaluator contract.
- It is not importable.
- It improves known tasks by hardcoding their names or artifacts.
- It removes logging needed for later diagnosis.
- It has no plausible failure mode or falsifiable claim.
- It cannot be rolled back without losing the previous best version.

## Mechanism Ideas

Use these as search axes, not as mandatory changes:

- Memory content: raw examples, lessons, failures, rules, contrastive pairs, summaries
- Retrieval: similarity, diversity, label coverage, recency, graph traversal, two-stage retrieval
- Prompt architecture: draft-verify, compare-contrast, label priming, tool-state snapshots
- Learning trigger: every batch, error-only, confidence-gated, epoch-level compression
- Tool scaffold: preflight environment snapshot, command batching, output filtering, completion checks
- State management: fast/slow memory, checkpoint restore, bounded context, deduplication

## Reporting

Keep iteration reports short and diagnostic. Include:

- changed mechanism
- score movement by dataset/task group
- likely reason for wins and regressions
- trace evidence
- next search implication

Do not claim convergence unless the user asks for analysis rather than another iteration.
