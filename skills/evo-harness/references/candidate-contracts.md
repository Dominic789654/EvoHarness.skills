# Candidate Contracts

Use one of these patterns or adapt to the project. Prefer existing local APIs over inventing a new abstraction.

## Memory System Contract

```python
class MemorySystem:
    def __init__(self, llm): ...
    def predict(self, input: str) -> tuple[str, dict]: ...
    def learn_from_batch(self, batch_results: list[dict]) -> None: ...
    def get_state(self) -> str: ...
    def set_state(self, state: str) -> None: ...
```

Validation:

```bash
python -c "from package.agents.candidate import *; print('OK')"
```

Candidate metadata:

```json
{
  "name": "candidate_name",
  "file": "agents/candidate_name.py",
  "hypothesis": "Changing mechanism X should improve metric Y because Z.",
  "axis": "retrieval|memory|prompt|tooling|state",
  "base_system": "baseline_or_frontier_name",
  "components": ["mechanism", "tradeoff"]
}
```

## Agent Harness Contract

```python
class AgentHarness(BaseAgent):
    async def run(self, instruction, environment, context) -> None: ...
```

Validation:

```bash
python -c "from agents.candidate_name import AgentHarness; print('OK')"
```

Candidate metadata:

```json
{
  "name": "candidate_name",
  "import_path": "agents.candidate_name:AgentHarness",
  "hypothesis": "Changing mechanism X should improve task success by reducing Y.",
  "changes": "Specific one-mechanism change.",
  "expected_efficiency": "Expected token/turn/cost/latency impact."
}
```

## Pending Eval File

Write candidates to the path used by the outer evaluator:

```json
{
  "iteration": 1,
  "candidates": []
}
```

Never include held-out test results or labels in this file.
