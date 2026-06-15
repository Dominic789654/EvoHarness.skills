# EvoHarness.skills

Codex skills for bounded auto-research in harness engineering.

EvoHarness turns code, traces, metrics, and candidate history into falsifiable harness hypotheses, executable candidate code, and held-out evaluation discipline.
It also treats harness evolution as a versioned research process: bad optimizations are kept for diagnosis but the active frontier can roll back to the best earlier version.

This repository currently contains:

- `skills/evo-harness`: a workflow skill for setting up and running bounded auto-research loops over task-specific harness code.

The skill is intended for narrow, benchmarkable harness surfaces such as memory systems, retrieval wrappers, prompt/context builders, and tool-use scaffolds. It is not a replacement for building a full production agent product or doing open-ended scientific research.

The bundled `plot_scores.py` script can turn `evolution_summary.jsonl` into a version-vs-eval-score chart for tracking the frontier over time.

## Install

Copy or symlink `skills/evo-harness` into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/evo-harness "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then invoke it with:

```text
Use $evo-harness to run bounded auto-research over this benchmark's harness.
```
