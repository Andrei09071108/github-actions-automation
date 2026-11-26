# Local setup

Install Git and Python 3.13 to match the workflow's major and minor version. The application and tests use the standard library. Extract the audit package, run `git clone repository.bundle queue-ci`, then enter queue-ci. Run `python -m unittest discover -s tests -v` from this directory so imports resolve.

In a disposable clone, switch with `git switch --detach origin/demo/regression` and repeat the command. Expect one failure. Switch to origin/demo/corrected and repeat; all four tests should pass. Return with `git switch main`. Inspect the exit status immediately after each run with `$LASTEXITCODE` in PowerShell or `echo $?` in a POSIX shell.
