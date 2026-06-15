# EvoHarness.skills

Codex skills for bounded auto-research in harness engineering.

EvoHarness turns code, traces, metrics, and candidate history into falsifiable harness hypotheses, executable candidate code, and held-out evaluation discipline.

This repository currently contains:

- `skills/evo-harness`: a workflow skill for setting up and running bounded auto-research loops over task-specific harness code.

The skill is intended for narrow, benchmarkable harness surfaces such as memory systems, retrieval wrappers, prompt/context builders, and tool-use scaffolds. It is not a replacement for building a full production agent product or doing open-ended scientific research.

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
