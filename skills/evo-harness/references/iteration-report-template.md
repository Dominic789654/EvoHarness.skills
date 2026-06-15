# Iteration Report Template

Keep reports under 30 lines.

## Iteration N

- Candidates:
- Baseline/frontier before eval:
- Best result after eval:
- Mechanism tested:
- Improved tasks or datasets:
- Regressed tasks or datasets:
- Trace evidence:
- Likely explanation:
- Cost/context/latency impact:
- Next implication:

## Example

- Candidates: `contrastive_memory`, `label_coverage_memory`
- Before: `fewshot_all` avg val 42.0
- After: `contrastive_memory` avg val 45.5
- Mechanism: retrieves near misses with different labels
- Improved: label-heavy tasks with recurring confusions
- Regressed: simple binary tasks, likely from excess context
- Trace evidence: prior failures confused adjacent labels; new prompt included discriminating examples
- Next implication: combine contrastive retrieval with stricter context budget
