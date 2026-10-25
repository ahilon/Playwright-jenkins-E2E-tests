# Playwright Jenkins E2E

End-to-end tests for Jenkins using Playwright, pytest, and a REST API client.

## Table of contents

- [Project objective](#project-objective)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Jenkins](#running-jenkins)
- [Running tests](#running-tests)
- [Playwright tools](#playwright-tools)
- [GitHub Actions](#github-actions)
- [Changelog](#changelog)

## Project objective

Practice testing Jenkins through its UI and REST API. The suite covers successful
and unsuccessful login, job creation and deletion, and running a freestyle build.

## Technologies

- Python
- Playwright and pytest-playwright
- pytest and pytest-xdist
- httpx
- Jenkins
- uv
- Docker Compose
- GitHub Actions (in progress)

## Requirements

- Python 3.12
- uv
- Docker with Docker Compose for the local Jenkins instance
- Chromium installed through Playwright

## Installation

From the repository root:

```bash
uv sync
uv run playwright install chromium
```

## Configuration

Create a `.env` file in the repository root:

```dotenv
JENKINS_URL=http://localhost:8080
JENKINS_USER=testuser
JENKINS_PASSWORD=testpass123
# Uncomment and fill in to enable REST tests:
# JENKINS_TOKEN=your-api-token
```

These credentials match the local Jenkins initialization script and are intended
for the test instance. The `.env` file is ignored by Git.

Generate an API token in the Jenkins user's settings and set `JENKINS_TOKEN` to
enable REST tests. REST tests are skipped when this variable is absent.

## Running Jenkins

Run these commands from the repository root:

```bash
# Validate the Compose configuration
docker compose -f docker/docker-compose.yaml config

# Start Jenkins and wait for the healthcheck to pass
docker compose -f docker/docker-compose.yaml up -d --wait

# Check container status
docker compose -f docker/docker-compose.yaml ps

# Follow logs (Ctrl+C stops following)
docker compose -f docker/docker-compose.yaml logs -f

# Stop and remove containers
docker compose -f docker/docker-compose.yaml down
```

Jenkins is available at `http://localhost:8080`. The initialization script creates
the test account and disables the setup wizard. The healthcheck checks `/login`;
starting the container does not immediately mean Jenkins is ready for tests.

## Running tests

Start Jenkins and configure `.env` first. Run commands from the repository root:

```bash
# All tests
uv run pytest

# Smoke tests
uv run pytest tests/smoke

# End-to-end tests (UI and REST)
uv run pytest tests/e2e

# One test file
uv run pytest tests/e2e/test_crud_cycle_ui.py

# Select tests by marker
uv run pytest -m smoke
uv run pytest -m e2e

# Show the browser
uv run pytest --headed

# Show the browser and slow down Playwright actions
uv run pytest --headed --slowmo 500

# Retain traces for failed tests
uv run pytest --tracing retain-on-failure
```

Run tests through pytest rather than executing test files directly. Pytest loads
the fixtures and Playwright options used by the suite.

## Playwright tools

Generate interactions against the local Jenkins instance:

```bash
uv run playwright codegen --lang en-US http://localhost:8080
```

Open a recorded trace (replace the path with the actual trace file):

```bash
uv run playwright show-trace test-results/<test-directory>/trace.zip
```

## GitHub Actions

Version 1.3 is in progress. The goal is to run Jenkins in a service container,
wait for readiness, and run tests against it on a Linux runner. CI also needs
Playwright's Chromium browser and its system dependencies.

## Changelog

### 1.3 — CI automation (in progress)

- Set up a GitHub Actions workflow.
- Planned: run Jenkins in a service container with a readiness check.
- Planned: run the test suite against Jenkins in CI.
- Planned: document Windows-to-Linux issues discovered during CI runs.

### 1.2 — Migration to pytest

- Refactor tests to use pytest.
- Introduce fixtures and shared test configuration.

### 1.1 — End-to-end tests

- Add Jenkins job scenarios through the UI and REST API.

### 1.0 — Initial Playwright tests

- Add initial sanity tests using Playwright.
