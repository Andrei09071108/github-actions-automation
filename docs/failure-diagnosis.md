# Diagnose the regression

The default deadline is inclusive. A request at 23 hours waits, a request at 24 hours qualifies, and a request at 25 hours also qualifies. The feature introduces a configurable limit. Its first revision uses a strict greater-than comparison. Open the failing test step and locate test_exact_limit: expected True, observed False.

Compare demo/regression with main and inspect the production predicate. Restore the inclusive comparison while retaining the configurable limit. Repeat the exact test command and compare the tests tree IDs across the three revisions. For a checkout or interpreter setup failure, inspect that earlier step first; the suite may never have started.
