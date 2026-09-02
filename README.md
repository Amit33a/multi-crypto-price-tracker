# Multi Crypto Price Tracker

A modern Python backend automation project that fetches real-time cryptocurrency prices from the CoinGecko API, stores historical prices in PostgreSQL running inside Docker, generates formatted reports, sends automated email reports, logs application activity, implements retry mechanisms with exponential backoff, supports scheduled execution, and follows professional Python development practices including automated testing, mocking, code coverage, formatting, linting, pre-commit hooks, dependency injection, and GitHub Actions Continuous Integration.

The project has been developed progressively from a simple Python script into a modular, testable backend application.

---

# Overview

This project demonstrates how to:

* Consume data from a public REST API.
* Handle temporary API failures using retry logic and exponential backoff.
* Validate API responses before processing data.
* Store cryptocurrency prices in PostgreSQL.
* Generate formatted cryptocurrency reports.
* Save reports to files.
* Send automated email reports with attachments.
* Log application events to both the console and log files.
* Manage configuration using environment variables.
* Validate required configuration values.
* Run PostgreSQL inside Docker.
* Automate execution using Windows Task Scheduler.
* Write automated unit tests using pytest and unittest.mock.
* Mock external dependencies during testing.
* Organise Python code into a modular package structure.
* Separate application orchestration from individual services.
* Use dependency injection to improve testability.
* Use an application factory pattern.
* Handle database transactions safely.
* Use context managers for database resources.
* Apply automated code formatting and linting.
* Generate code coverage reports.
* Enforce minimum test coverage.
* Run Continuous Integration using GitHub Actions.
* Build a maintainable, testable Python backend application.

---

# Project Architecture

The project evolved from a collection of Python scripts into a layered application architecture.

```text
                         run.py
                           │
                           ▼
                  app/api/main.py
               Application Factory
                           │
                           ▼
              app/api/dependencies.py
                 Dependency Wiring
                           │
                           ▼
          app/services/crypto_workflow.py
                Workflow Orchestration
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   fetch_crypto.py      db.py           report.py
          │                │                │
          ▼                ▼                ▼
   CoinGecko API      PostgreSQL       Report Text
                       Docker
                                           │
                                           ▼
                                  email_sender.py
                                           │
                                           ▼
                                      SMTP Server
```

The application also uses:

```text
app/config/settings.py
        │
        ▼
Environment Configuration


app/utils/logger.py
        │
        ▼
Centralised Application Logging
```

---

# Application Flow

The complete application workflow is:

```text
Application Start
       │
       ▼
Load Configuration
       │
       ▼
Create Application
       │
       ▼
Create Database Table
       │
       ▼
Fetch Cryptocurrency Prices
       │
       ▼
Validate API Response
       │
       ▼
Save Prices to PostgreSQL
       │
       ▼
Retrieve Historical Prices
       │
       ▼
Generate Report
       │
       ▼
Print Report
       │
       ▼
Save Report to File
       │
       ▼
Send Report by Email
       │
       ▼
Log Result
       │
       ▼
Application Finished
```

---

# Features

## API Integration

The application uses the CoinGecko API to retrieve cryptocurrency prices.

Currently tracked cryptocurrencies:

* Bitcoin (BTC)
* Ethereum (ETH)
* Solana (SOL)
* Binance Coin (BNB)

Features include:

* REST API integration using Requests.
* Configurable request timeout.
* HTTP status validation.
* Safe JSON extraction.
* API response validation.
* Detection of missing cryptocurrency data.
* Automatic retry mechanism.
* Exponential backoff.
* Configurable maximum retry attempts.
* Logging of API request attempts.
* Handling of connection failures.
* Handling of timeout errors.
* Handling of HTTP errors.
* Handling of invalid JSON responses.

---

# Database Integration

The application uses PostgreSQL for persistent cryptocurrency price storage.

PostgreSQL runs inside Docker.

Database features include:

* PostgreSQL integration using psycopg2.
* Automatic table creation.
* Historical price storage.
* Timestamped records.
* Database transaction handling.
* Transaction rollback on errors.
* Automatic connection cleanup.
* Automatic cursor cleanup.
* Context manager support.
* Database error handling.
* Separate database service functions.

---

# Database Schema

```sql
CREATE TABLE IF NOT EXISTS multi_crypto_price (
    id SERIAL PRIMARY KEY,
    crypto_name VARCHAR(50) NOT NULL,
    price_usd NUMERIC(18,8) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Report Generation

The application generates a formatted cryptocurrency price report.

Features include:

* Historical price reporting.
* Timestamped reports.
* Human-readable formatting.
* Terminal output.
* Text-file output.
* Centralised report configuration.
* Report generation logging.

Generated report:

```text
reports/crypto_report.txt
```

Example:

```text
CRYPTO PRICE REPORT
==============================
Generated at: 2026-07-05 09:15:21

Bitcoin      $62553.00
Ethereum     $1564.41
Solana       $153.77
Binancecoin  $564.38
```

---

# Email Automation

The application automatically sends the generated report through SMTP.

Features include:

* SMTP integration.
* TLS connection.
* Authentication.
* Plain-text email.
* Report attachment.
* Configurable sender.
* Configurable receiver.
* Email error handling.
* Email activity logging.

The generated report is attached to the email.

---

# Scheduling

The application supports automated execution using Windows Task Scheduler.

A scheduled execution can automatically:

1. Fetch cryptocurrency prices.
2. Store prices in PostgreSQL.
3. Retrieve historical prices.
4. Generate a report.
5. Save the report.
6. Send the report by email.
7. Record execution details in the log.

Scheduling documentation:

```text
docs/windows_task_scheduler.md
```

---

# Logging

The project uses a centralised logger.

Logging features include:

* Console logging.
* File logging.
* INFO level logging.
* WARNING level logging.
* ERROR level logging.
* API request logging.
* Database operation logging.
* Report generation logging.
* Email operation logging.
* Application lifecycle logging.
* Error logging.
* Retry-attempt logging.

The logger is defined in:

```text
app/utils/logger.py
```

Generated log:

```text
logs/app.log
```

---

# Configuration

Application configuration is managed using environment variables and `python-dotenv`.

Configuration is centralised in:

```text
app/config/settings.py
```

The application validates required environment variables during configuration loading.

Configuration includes:

* Database host
* Database port
* Database name
* Database username
* Database password
* API request timeout
* Maximum API retry attempts
* Email host
* Email port
* Email username
* Email password
* Email receiver
* Report directory
* Report filename
* Report path

---

# Environment Variables

Create a `.env` file in the project root.

```env
# Database
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=crypto_tracker

# API
REQUEST_TIMEOUT=10
MAX_RETRIES=3

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver@gmail.com
```

Never commit the real `.env` file to GitHub.

---

# Project Structure

The project currently follows a modular package-based architecture.

```text
multi-crypto-price-tracker/
│
├── app/
│   │
│   ├── api/
│   │   ├── dependencies.py
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── __init__.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── crypto_workflow.py
│   │   ├── email_sender.py
│   │   ├── fetch_crypto.py
│   │   ├── report.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── tests/
│   ├── test_crypto_workflow.py
│   ├── test_db.py
│   ├── test_email_sender.py
│   ├── test_fetch_crypto.py
│   ├── test_main.py
│   └── test_report.py
│
├── docs/
│   └── windows_task_scheduler.md
│
├── reports/
│   └── crypto_report.txt
│
├── logs/
│   └── app.log
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .coveragerc
├── .env.example
├── .env.test
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── run.py
└── README.md
```

`reports/` and `logs/` are runtime directories and are excluded from Git using `.gitignore`.

---

# Application Architecture

## Application Factory

The application uses an application factory pattern.

```text
app/api/main.py
```

The `create_application()` function creates the application entry point.

This makes the application easier to:

* Test.
* Configure.
* Extend.
* Integrate with other systems.
* Run with different dependencies.

---

## Dependency Injection

Application dependencies are centralised in:

```text
app/api/dependencies.py
```

Dependencies include:

* Logger
* Database table creation
* Cryptocurrency price fetching
* Database insertion
* Database retrieval
* Report generation
* Email sending

The workflow receives these dependencies explicitly.

This allows tests to replace real services with mocks without making real API, database, or email calls.

---

## Workflow Service

The main business workflow is contained in:

```text
app/services/crypto_workflow.py
```

The workflow coordinates:

1. Database initialisation.
2. Cryptocurrency price fetching.
3. Database insertion.
4. Database retrieval.
5. Report generation.
6. Report output.
7. Report file creation.
8. Email delivery.

The workflow returns:

```python
True
```

when the complete workflow succeeds.

It returns:

```python
False
```

when a controlled workflow failure occurs.

Unexpected workflow exceptions are logged and handled safely.

---

# Running the Application

The application entry point is:

```text
run.py
```

Run the application with:

```bash
python run.py
```

The launcher creates the application and executes it.

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd multi-crypto-price-tracker
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

## 3. Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure environment variables

Copy:

```text
.env.example
```

to:

```text
.env
```

Then update the configuration values.

## 6. Start PostgreSQL

```bash
docker compose up -d
```

## 7. Run the application

```bash
python run.py
```

---

# Docker Setup

PostgreSQL is containerised using Docker.

Start PostgreSQL:

```bash
docker compose up -d
```

Verify the container:

```bash
docker ps
```

Stop PostgreSQL:

```bash
docker compose down
```

---

# Testing

The project uses:

* pytest
* unittest.mock
* pytest-cov

The test suite currently contains **18 automated tests**.

Tests cover:

* Cryptocurrency API success scenarios.
* Cryptocurrency API failure scenarios.
* Request timeouts.
* HTTP errors.
* Invalid JSON responses.
* Missing API data.
* Retry behaviour.
* Database connection.
* Database operations.
* Database connection failures.
* Database transaction behaviour.
* Report generation.
* Email sending.
* Crypto workflow success.
* Crypto workflow failure.
* Unexpected workflow errors.
* Application success handling.
* Application failure handling.
* Application exception handling.

Run the complete test suite:

```bash
pytest
```

Expected current result:

```text
18 passed
```

---

# Test Coverage

Generate terminal coverage:

```bash
pytest --cov --cov-report=term-missing
```

The project currently achieves approximately **81% test coverage**.

The CI pipeline enforces a minimum coverage requirement of:

```text
60%
```

Generate an HTML coverage report:

```bash
pytest --cov --cov-report=html
```

Open:

```text
htmlcov/index.html
```

to inspect detailed line-by-line coverage.

---

# Mocking and Testability

The project uses `unittest.mock` to isolate application components during testing.

Examples include mocking:

* External API calls.
* Database operations.
* Email sending.
* File operations.
* Application dependencies.
* Workflow execution.

This prevents unit tests from depending on:

* Internet access.
* A real SMTP server.
* A real database.
* Actual email delivery.
* Runtime files.

Dependency injection was introduced specifically to make this isolation cleaner and easier.

---

# Code Quality

The project follows modern Python development practices.

## Black

Black is used for automatic Python code formatting.

Check formatting:

```bash
black --check .
```

Format the project:

```bash
black .
```

---

## Ruff

Ruff is used for linting and static code analysis.

Run:

```bash
ruff check .
```

---

## isort

isort is used to maintain consistent import ordering.

Check imports:

```bash
isort . --check-only
```

---

## Pre-commit

Pre-commit hooks are configured to help maintain code quality before commits.

The hooks help check:

* Import ordering.
* Code formatting.
* Static analysis.

Run all hooks manually:

```bash
pre-commit run --all-files
```

---

# Continuous Integration

The project uses GitHub Actions for Continuous Integration.

Workflow file:

```text
.github/workflows/ci.yml
```

The CI pipeline runs automatically on:

* Pushes to the `main` branch.
* Pull requests targeting the `main` branch.

The pipeline performs:

1. Repository checkout.
2. Python environment setup.
3. Dependency installation.
4. isort verification.
5. Black formatting verification.
6. Ruff linting.
7. Test environment creation.
8. pytest execution.
9. Test coverage measurement.
10. Minimum coverage enforcement.

The current minimum coverage requirement is:

```text
60%
```

---

# Error Handling

The project implements error handling across the major application components.

## API

Handles:

* Connection errors.
* Timeout errors.
* HTTP errors.
* Invalid JSON.
* Missing cryptocurrency data.
* Temporary API failures.
* Retry attempts.
* Exponential backoff.

---

## Database

Handles:

* Database connection failures.
* SQL errors.
* Transaction failures.
* Transaction rollback.
* Resource cleanup.
* Context-managed database connections.

---

## Email

Handles:

* SMTP connection failures.
* Authentication failures.
* Email sending failures.
* Attachment-related errors.

---

## Application

The application handles:

* Workflow failures.
* Unexpected exceptions.
* Application lifecycle logging.

The workflow returns a success/failure status to the application layer.

---

# Retry Mechanism

The CoinGecko API integration includes retry logic.

The application can retry failed API requests up to the configured number of attempts.

Example configuration:

```env
MAX_RETRIES=3
```

The application also uses exponential backoff between retry attempts.

This reduces the chance of immediately repeating a request when an external API is temporarily unavailable.

---

# Professional Backend Practices Implemented

The project currently demonstrates:

* Modular Python architecture.
* Separation of responsibilities.
* Service-layer organisation.
* Application factory pattern.
* Dependency injection.
* Centralised dependency wiring.
* Environment-based configuration.
* Configuration validation.
* Type hints.
* Database transactions.
* Context managers.
* Automatic resource cleanup.
* Retry mechanisms.
* Exponential backoff.
* Structured application logging.
* Console and file logging.
* Automated testing.
* Mocking.
* Test isolation.
* Code coverage.
* Coverage quality gates.
* Black formatting.
* Ruff linting.
* isort import management.
* Pre-commit hooks.
* GitHub Actions CI.
* Dockerised PostgreSQL.
* Professional Git commit history.

---

# Development Stages

The project has been developed progressively rather than being built as one large application.

## Stage 1 — Basic Cryptocurrency API Integration

Built the initial Python application that:

* Connected to CoinGecko.
* Retrieved Bitcoin price data.
* Parsed API responses.
* Displayed cryptocurrency information.

---

## Stage 2 — Multiple Cryptocurrency Support

Expanded the application to track multiple cryptocurrencies:

* Bitcoin
* Ethereum
* Solana
* Binance Coin

---

## Stage 3 — Error Handling

Introduced error handling for:

* Connection failures.
* HTTP errors.
* Invalid responses.
* Missing data.
* JSON parsing problems.

---

## Stage 4 — Retry Mechanism

Introduced:

* Retry logic.
* Configurable retry attempts.
* Request timeouts.
* Exponential backoff.

---

## Stage 5 — PostgreSQL Database

Introduced persistent storage using PostgreSQL.

The application began storing historical cryptocurrency prices.

---

## Stage 6 — Docker

PostgreSQL was containerised using Docker.

This provided a consistent local database environment.

---

## Stage 7 — Reporting

Introduced report generation.

The application can:

* Retrieve historical data.
* Generate formatted reports.
* Display reports in the terminal.
* Save reports to files.

---

## Stage 8 — Email Automation

Introduced automated email delivery.

The generated report can be attached and sent through an SMTP server.

---

## Stage 9 — Logging and Configuration

Introduced:

* Centralised configuration.
* `.env` support.
* Configuration validation.
* Console logging.
* File logging.
* Application lifecycle logging.

---

## Stage 10 — Testing and Code Quality

Introduced professional development practices including:

* pytest.
* unittest.mock.
* pytest-cov.
* Black.
* Ruff.
* isort.
* pre-commit.
* GitHub Actions.
* Automated CI.
* Coverage enforcement.

---

## Stage 11 — Application Architecture and Testability

Stage 11 focused on turning the collection of scripts into a more maintainable backend application.

Major improvements included:

* Moving application code into the `app/` package.
* Separating API/application responsibilities.
* Introducing an application factory.
* Creating a dedicated workflow service.
* Introducing dependency injection.
* Centralising application dependencies.
* Making the application entry point testable.
* Adding dedicated workflow tests.
* Adding application-level tests.
* Improving workflow success/failure handling.
* Handling unexpected workflow exceptions.
* Mocking report file operations in tests.
* Improving test isolation.
* Maintaining automated code quality checks.
* Verifying the complete application workflow end-to-end.

Current Stage 11 test status:

```text
18 tests passed
Approximately 81% code coverage
Ruff: Passed
Black: Passed
isort: Passed
GitHub Actions CI: Passed
```

---

# Current Development Status

The project has successfully progressed from a basic Python API script into a modular backend automation application.

Current architecture:

```text
Python Application
       │
       ├── Configuration
       │
       ├── API Integration
       │
       ├── Retry & Resilience
       │
       ├── PostgreSQL
       │
       ├── Reporting
       │
       ├── Email Automation
       │
       ├── Logging
       │
       ├── Dependency Injection
       │
       ├── Automated Testing
       │
       ├── Code Coverage
       │
       ├── Code Quality
       │
       ├── Docker
       │
       └── GitHub Actions CI
```

---

# Generated Files

Report:

```text
reports/crypto_report.txt
```

Application log:

```text
logs/app.log
```

HTML coverage report:

```text
htmlcov/index.html
```

---

# Git Development Workflow

The project is developed incrementally using small, focused Git commits.

Examples of recent architectural commits include:

```text
refactor: move service layer into services package
refactor: move application entry point into api package
refactor: add application launcher script
refactor: inject logger into report service
refactor: introduce application factory
refactor: extract crypto workflow service
test: add crypto workflow unit tests
refactor: return workflow execution status
test: strengthen crypto workflow unit tests
refactor: add return type to crypto workflow
feat: handle unexpected workflow failures
refactor: centralize application dependencies
test: make application entry point testable
```

This approach keeps the development history understandable and demonstrates the progression of the application architecture.

---

# Technologies Used

## Backend

* Python 3.14
* Requests

## Database

* PostgreSQL
* psycopg2

## Containerisation

* Docker
* Docker Compose

## Email

* smtplib
* email.message.EmailMessage

## Configuration

* python-dotenv

## Testing

* pytest
* unittest.mock
* pytest-cov

## Code Quality

* Black
* Ruff
* isort
* pre-commit

## CI/CD

* GitHub Actions

## Scheduling

* Windows Task Scheduler

## Version Control

* Git
* GitHub

---

# Future Improvements

Potential future development areas include:

* CSV report export.
* Excel report export.
* HTML email reports.
* Summary statistics.
* REST API using FastAPI.
* Interactive dashboard.
* Dockerisation of the Python application.
* Multi-stage Docker builds.
* Linux cron scheduling.
* Integration testing.
* Database migrations using Alembic.
* Health check endpoints.
* Prometheus metrics.
* Grafana dashboards.
* Structured JSON logging.
* Secrets management.
* Monitoring and alerting.
* CI/CD deployment pipeline.
* Cloud deployment.

These are future possibilities and are **not part of the current Stage 11 implementation**.

---

# Learning Outcomes

This project has been used to develop practical backend engineering skills in:

* REST API integration.
* HTTP request handling.
* Retry and resilience patterns.
* PostgreSQL.
* Docker.
* Database transactions.
* Context managers.
* SMTP email automation.
* Logging.
* Environment configuration.
* Configuration validation.
* Error handling.
* Modular architecture.
* Application factory patterns.
* Dependency injection.
* Service-layer design.
* Automated testing.
* Mocking.
* Test isolation.
* Code coverage.
* Formatting.
* Linting.
* Pre-commit automation.
* Continuous Integration.
* Professional Git workflow.
* Production-oriented Python development.

---

# Author

**Amit Sharma**

Aspiring Python Backend Developer

GitHub:

```text
https://github.com/Amit33a
```

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
