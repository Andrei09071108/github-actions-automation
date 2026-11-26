# GitHub Actions Automation

[![Continuous integration](https://github.com/Andrei09071108/github-actions-automation/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Andrei09071108/github-actions-automation/actions/workflows/ci.yml)

## Automated Testing & Continuous Integration

An independent, AI-assisted single-author portfolio project for a fictional support team. A request qualifies for follow-up as soon as it reaches its deadline. Adding a configurable limit introduced an off-by-one-boundary error: the request at exactly 24 hours stopped qualifying. The [pull request](https://github.com/Andrei09071108/github-actions-automation/pull/1) records the failed check and the fix before integration.

| Stage | Event | Revision | Result |
|---|---|---|---|
| [Baseline](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45894999405) | push | 914da99 | success |
| [Controlled regression](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895112131) | pull_request | 8a3573f | failure |
| [Correction](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895181336) | pull_request | 0b9578b | success |
| [Merged main](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895220263) | push | 6ec8c17 | success |
| [Manual dispatch](https://github.com/Andrei09071108/github-actions-automation/actions/runs/45895261446) | workflow_dispatch | 6ec8c17 | success |

Run `python -m unittest discover -s tests -v` to reproduce the four checks. See the [setup guide](docs/setup.md), [workflow guide](docs/ci-workflow.md), [failure diagnosis](docs/failure-diagnosis.md) and [handover](docs/handover.md). The workflow runs tests only. There is no production deployment.
