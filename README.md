# Playwright Jenkins E2E

The goal of the project is to write Jenkins end-to-end tests using Playwright.

## Table of contents

- [Project objective](#project-objective)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project structure](#project-structure)
- [Running tests](#running-tests)
- [Reports](#reports)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Best practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)

## project objective


## Technologies

- Python
- Playwright
- pytest
- pytest-playwright
- pytest-xdist
- Jenkins
- uv
- Docker

## Requirements

- Python `3.12`
- uv
- A running Jenkins instance
- Chromium browser installed
- Access to a test account

## Installation

```bash
git clone <repository-url>
cd playwright-jenkins-e2e

uv sync
uv run playwright install chromium
```

## Playwright
uv run python -m playwright codegen --lang en-US  http://localhost:8080  - generate code for test
uv run python -m pytest - run tests
uv run python tests/test_smoke.py - run actual recored test

## test arguments

# simple fast tests
uv run python tests/smoke/test_smoke.py

# slower, headed tests with slowmo set to 500
uv run python tests/smoke/test_smoke.py --debug

# tracing on 
uv run python tests/smoke/test_smoke.py --tracing on

# both
uv run python tests/smoke/test_smoke.py --debug --tracing on

## Docker
- cd docker
- docker compose config          # validate syntax and show the resolved - - - configuration
- docker compose up -d           # start in detached mode
- docker compose ps              # show status, including health
- docker compose logs -f         # follow logs in real time
- docker compose down            # stop the services
- docker compose down -v         # stop the services and remove volumes