# How the checks run

Continuous integration gives contributors feedback by running agreed checks against proposed and integrated changes. An event starts a workflow, the automation described by the YAML file. Its single job groups three ordered steps on one runner, the Ubuntu virtual machine that executes them. YAML indentation places the steps under the job; the quoted Python version is a string.

A push to main checks the integrated revision. A pull request targeting main checks the proposed merge when opened, reopened or updated. A feature push without an open PR does not match the main push filter. Manual dispatch becomes available once the workflow exists on the default branch.

Checkout supplies the source tree, setup-python selects Python 3.13, and unittest returns the process status directly. A zero exit marks the test step successful; a non-zero exit fails the step and job. In Actions, open the run for the expected event and commit, select **Follow-up regression tests**, then expand **Run follow-up regression tests**. A failed check is a review signal. Enforcing a merge block requires a separately configured repository rule.

The job has read-only contents access, does not persist checkout credentials, and uses the ordinary pull_request event. Official actions are pinned to full commit IDs. The runner is the standard Ubuntu 24.04 image; Python patch and image updates can change over time.

The [published workflow](https://github.com/Andrei09071108/github-actions-automation/actions/workflows/ci.yml) ran on main pushes, pull requests to main and manual dispatch. The baseline runner used Ubuntu 24.04 and Python 3.13.18. Each recorded job used the standard hosted runner.
