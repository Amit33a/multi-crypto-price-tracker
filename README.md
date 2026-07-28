# Multi Crypto Price Tracker

A modern Python backend automation project that fetches real-time cryptocurrency prices from the CoinGecko API, stores them in a PostgreSQL database running inside Docker, generates formatted reports, sends automated email reports, logs application activity, implements retry mechanisms with exponential backoff, supports scheduled execution, and follows professional Python development practices including automated testing, code formatting, linting, pre-commit hooks, code coverage, and GitHub Actions Continuous Integration.

---

# Overview

This project demonstrates how to:

- Consume data from a public REST API.
- Handle temporary API failures using retry logic and exponential backoff.
- Validate API responses before processing data.
- Store cryptocurrency prices in PostgreSQL.
- Generate formatted reports.
- Send automated email reports with attachments.
- Log application events to both the console and log files.
- Manage configuration using environment variables.
- Run PostgreSQL inside Docker.
- Automate execution using Windows Task Scheduler.
- Write automated unit tests using pytest and unittest.mock.
- Organise Python code into reusable modules.
- Handle database transactions safely.
- Build a maintainable backend application.
- Perform automated code quality checks.
- Generate code coverage reports.
- Run Continuous Integration using GitHub Actions.

---

# Project Architecture

```
                    CoinGecko API
                          │
                          ▼
                 fetch_crypto.py
                          │
                          ▼
                   Validate Response
                          │
                          ▼
                       PostgreSQL
                   (Docker Container)
                          │
                          ▼
                      report.py
                          │
                          ▼
                  crypto_report.txt
                          │
                          ▼
                  email_sender.py
                          │
                          ▼
                      SMTP Server
                          │
                          ▼
                    Email Receiver

```

Windows Task Scheduler can automatically execute the application on a schedule.

---

# Features

## API Integration

- Fetch real-time cryptocurrency prices from the CoinGecko API.
- Track multiple cryptocurrencies:
  - Bitcoin (BTC)
  - Ethereum (ETH)
  - Solana (SOL)
  - Binance Coin (BNB)
- HTTP request handling using Requests.
- Configurable request timeout.
- HTTP status validation.
- Safe JSON extraction.
- Automatic retry mechanism.
- Exponential backoff between retries.
- Configurable retry attempts.
- API response validation.
- Detection of missing cryptocurrency data.

---

## Database Integration

- PostgreSQL integration using psycopg2.
- Dockerised PostgreSQL using Docker Compose.
- Automatic table creation.
- Historical cryptocurrency price storage.
- Timestamped records.
- Database transaction management.
- Automatic cleanup of database resources.
- Context manager support for database connections.

---

## Report Generation

- Generate formatted cryptocurrency reports.
- Display reports in the terminal.
- Save reports as text files.
- Timestamp every generated report.
- Centralised report file configuration.

---

## Email Automation

- SMTP email integration.
- Secure TLS connection.
- Plain text email support.
- Automatic report delivery.
- Report attachment support.
- Configurable sender and receiver.

---

## Scheduling

- Automated execution using Windows Task Scheduler.
- Daily or custom schedules.
- Automatically:
  - Fetches cryptocurrency prices.
  - Updates PostgreSQL.
  - Generates reports.
  - Sends email reports.
  - Logs execution.

---

## Logging

- Centralised logger configuration.
- File logging.
- Console logging.
- INFO, WARNING and ERROR log levels.
- API logging.
- Database logging.
- Email logging.
- Report generation logging.
- Application lifecycle logging.

---

## Configuration

Environment variables are managed using `.env`.

Configuration includes:

- Database settings
- Email settings
- API timeout
- Retry attempts
- Report path

---

## Code Quality

The project uses:

- Ruff
- Black
- isort
- pre-commit
- Consistent Python formatting
- Automatic formatting before every commit

---

## Continuous Integration

GitHub Actions automatically performs:

- Ruff linting
- Black formatting verification
- isort import verification
- Unit testing
- Code coverage reporting
- Minimum coverage enforcement

---

## Testing

The project includes automated unit tests using **pytest** and **unittest.mock**.

Current test coverage includes:

- Report generation
- CoinGecko API integration
- Database connection
- Database insert operations
- Database retrieval
- API success and failure scenarios
- Email sending
- Database connection failures

Run all tests:

```bash
pytest
```

Generate terminal coverage:

```bash
pytest --cov --cov-report=term-missing
```

Generate HTML coverage:

```bash
pytest --cov --cov-report=html
```

Open:

```
htmlcov/index.html
```

to inspect detailed line-by-line coverage.

---

# Project Structure

```text
multi-crypto-price-tracker/
│
├── fetch_crypto.py
├── db.py
├── report.py
├── email_sender.py
├── logger_config.py
├── config.py
├── main.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── tests/
│   ├── test_db.py
│   ├── test_fetch_crypto.py
│   ├── test_report.py
│   └── test_email_sender.py
│
├── docs/
│   └── windows_task_scheduler.md
│
├── reports/
├── logs/
│
├── .coveragerc
├── .env.example
├── .env.test
├── .pre-commit-config.yaml
├── pyproject.toml
├── pytest.ini
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

## Backend

- Python 3.14
- Requests

### Database

- PostgreSQL
- psycopg2

### Containerisation

- Docker
- Docker Compose

### Email

- smtplib
- EmailMessage

### Testing

- pytest
- unittest.mock
- pytest-cov

### Code Quality

- Ruff
- Black
- isort
- pre-commit

### DevOps

- GitHub Actions
- Windows Task Scheduler

### Configuration

- python-dotenv

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

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure environment variables

Copy:

```
.env.example
```

to

```
.env
```

and update the values.

## 6. Start PostgreSQL

```bash
docker compose up -d
```

## 7. Run the application

```bash
python main.py
```

---

# Docker Setup

Start PostgreSQL:

```bash
docker compose up -d
```

Verify the container is running:

```bash
docker ps
```

Stop PostgreSQL:

```bash
docker compose down
```

---

# Scheduling

The project supports automated execution using **Windows Task Scheduler**.

Each scheduled execution automatically:

1. Fetches cryptocurrency prices from CoinGecko.
2. Stores prices in PostgreSQL.
3. Generates a formatted report.
4. Saves the report to disk.
5. Sends the report by email.
6. Records execution details in the application log.

See:

```text
docs/windows_task_scheduler.md
```

for the complete scheduling guide.

---

# Example Report

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

# Generated Files

Generated report:

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

# Error Handling

The project implements robust error handling across multiple components.

## API

- Connection failures
- Request timeout handling
- HTTP status validation
- Invalid JSON responses
- Missing cryptocurrency validation
- Retry mechanism
- Exponential backoff

## Database

- Database connection failures
- SQL execution errors
- Transaction rollback
- Automatic resource cleanup
- Safe connection management using context managers

## Email

- SMTP connection failures
- Authentication failures
- Email sending failures
- Attachment handling failures

## Application

- Centralized exception logging
- Graceful error reporting
- Application lifecycle logging

---

# Code Quality

The project follows modern Python development practices.

## Formatting

- Black
- Ruff Formatter

## Linting

- Ruff

## Import Management

- isort

## Pre-commit Hooks

Before every commit, the project automatically:

- Checks import order
- Checks formatting
- Formats code automatically when possible
- Runs static analysis

This helps maintain a clean and consistent codebase.

---

# Testing

The project includes automated unit tests using:

- pytest
- unittest.mock
- pytest-cov

Current test coverage includes:

- Report generation
- API success scenarios
- API failure scenarios
- Invalid JSON responses
- Missing API data
- Database connection
- Database insert operations
- Database retrieval
- Database connection failures
- Email sending

Generate a terminal coverage report:

```bash
pytest --cov --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov --cov-report=html
```

The CI pipeline also enforces a minimum code coverage threshold to help maintain code quality over time.

---

# Continuous Integration

The project uses **GitHub Actions** to automatically validate every push and pull request.

The workflow performs:

- Dependency installation
- Import sorting verification
- Code formatting verification
- Ruff linting
- Unit testing
- Code coverage verification

This ensures that only code meeting the project's quality standards passes the CI pipeline.

---

# Production Practices

This project incorporates several practices commonly used in professional Python backend development.

- Modular project architecture
- Environment-based configuration
- Configuration validation
- Reusable helper functions
- Centralized configuration management
- Type hints
- Context managers
- Automatic resource cleanup
- Retry mechanism with exponential backoff
- Database transaction safety
- Structured logging
- Dual logging handlers (file and console)
- Automated testing
- Mocking external services
- Code coverage reporting
- Coverage quality gates
- Automated formatting
- Automated linting
- Continuous Integration
- Dockerized database

---

# Learning Outcomes

This project was built to strengthen practical backend development skills, including:

- REST API integration
- PostgreSQL
- Docker
- Database transactions
- SMTP email automation
- Logging
- Environment variable management
- Error handling
- Retry and resilience patterns
- Context managers
- Type hints
- Automated testing
- Mocking external dependencies
- Code coverage
- Continuous Integration
- Professional Git workflow
- Production-oriented Python development

---

# Future Improvements

Possible future enhancements include:

- CSV report export
- Excel report export
- HTML email reports
- Summary statistics
- Interactive dashboard using Streamlit
- Dockerize the Python application
- Multi-stage Docker build
- Deploy to a cloud platform (AWS, Azure, or Render)
- Linux cron scheduling
- Integration testing
- REST API using FastAPI
- Prometheus metrics
- Grafana dashboards
- Structured JSON logging
- Database migrations using Alembic
- Secrets management
- Health check endpoint
- Monitoring and alerting
- CI/CD deployment pipeline

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