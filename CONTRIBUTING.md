# Developer guide

## Setup and local checks

Run `uv sync` after cloning, pulling dependency changes, or updating the project
version. This installs dependencies and updates `uv.lock` when needed.

Before opening a pull request, run:

```bash
uv sync
uv run ruff check .
uv run ruff format --check .
```

To apply automatic lint fixes and formatting, run:

```bash
uv run ruff check . --fix
uv run ruff format .
```

Review the resulting diff before committing. Ruff lint and formatting checks
must pass before merging. Configure the Ruff CI check as required in the `main`
ruleset; this guide alone does not enforce merge restrictions.

## Pull requests and reviews

- Check [CODEOWNERS](.github/CODEOWNERS) for ownership and reviewers.
- At least one approval is required, including approval from an applicable code
  owner when code owner review is enabled. Authors cannot approve their own PRs.
- New commits that change the PR diff dismiss previous approvals and require
  another review.
- Keep the PR branch up to date with `main`. Use **Update branch** on GitHub or
  update locally, resolving conflicts if necessary. Required checks must pass
  after the update.
- Merge using **Squash and merge** only.

These requirements must also be enabled in the repository's GitHub settings.

## E2E tests

For changes to application code or tests, add the `e2e_tests` label to the PR.
Adding the label starts the E2E workflow, which runs Jenkins in Docker and tests
against it. E2E checks are recommended and are not required checks for merging.

The current workflow runs when the label is added, not on every subsequent push.
After changing code, remove and re-add the label to test the latest revision.
Check the run results, including skipped tests, before marking E2E as executed.

For documentation-only changes, select **E2E tests not needed** in the PR
description and briefly explain why. Otherwise, select **Executed E2E tests**
after the run finishes and summarize the result.

## Versioning and changelog

Before merging a versioned change, update `[project].version` in
`pyproject.toml`. Use `MAJOR.MINOR.PATCH`, following this project's convention:

| Part | When to increment | Example |
| --- | --- | --- |
| Major | Major code changes, a major release, or a large refactor | `1.4.0` to `2.0.0` |
| Minor | New functionality | `2.0.0` to `2.1.0` |
| Patch | Bug fixes and small maintenance changes | `2.1.0` to `2.1.1` |

Reset the parts to the right when incrementing major or minor. For major and
minor changes, add a short entry to the [README changelog](README.md#changelog).

After editing the version or dependencies, run `uv sync` and commit both
`pyproject.toml` and `uv.lock`. CI should use `uv sync --locked` to detect a stale
lockfile.
