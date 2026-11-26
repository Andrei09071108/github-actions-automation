# Hosted acceptance

| Stage | Event | Revision | Result |
|---|---|---|---|
| [Baseline](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45894999405) | push | 914da99 | success |
| [Controlled regression](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895112131) | pull_request | 8a3573f | failure |
| [Correction](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895181336) | pull_request | 0b9578b | success |
| [Merged main](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895220263) | push | 6ec8c17 | success |
| [Manual dispatch](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895261446) | workflow_dispatch | 6ec8c17 | success |

The same four tests ran throughout. Only test_exact_limit failed on the feature regression. Contents are read-only in the job, and checkout does not persist credentials. Review was performed by the author. The independently audited local package predates the hosted demonstration.
