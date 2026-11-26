# Acceptance criteria

- The workflow covers main pushes, pull requests to main and manual dispatch.
- The single read-only job checks out code, sets up Python and runs unittest with its exit code intact.
- Baseline and corrected states pass four tests. Only the boundary test fails on the regression revision.
- The original tests and workflow are identical in all three states.
- The private bundle reproduces each result in a clean clone.
- Hosted acceptance requires real run links for baseline, failed PR, corrected PR and merged main.

Local observations accompany the audit package.
