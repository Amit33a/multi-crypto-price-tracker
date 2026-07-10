# Multi Crypto Price Tracker

A production-style Python backend automation project that fetches real-time cryptocurrency prices from the CoinGecko API, stores them in a PostgreSQL database running inside Docker, generates formatted reports, sends automated email reports, logs application activity, implements retry mechanisms with exponential backoff, supports scheduled execution, and includes unit tests for core modules.

---

# Overview

This project demonstrates how to:

* Consume data from a public REST API.
* Handle temporary API failures using retry logic and exponential backoff.
* Validate API responses before processing data.
* Store cryptocurrency prices in PostgreSQL.
* Generate formatted text reports.
* Send automated email reports with attachments.
* Log application events to both the console and log files.
* Manage configuration using environment variables.
* Run PostgreSQL inside Docker.
* Automate execution using Windows Task Scheduler.
* Write unit tests using pytest and unittest.mock.
* Organize Python code into reusable modules.
* Handle database transactions safely.
* Build a production-style backend application.

---

# Features

## API Integration

* Fetch real-time cryptocurrency prices from the CoinGecko API.
* Track multiple cryptocurrencies:

  * Bitcoin (BTC)
  * Ethereum (ETH)
  * Solana (SOL)
  * Binance Coin (BNB)
* HTTP request handling using Requests.
* Configurable request timeout.
* HTTP status validation.
* Safe JSON extraction.
* Automatic retry mechanism.
* Exponential backoff between retries.
* Configurable retry attempts.
* API response validation.
* Detection of missing cryptocurrency data.

---

## Database Integration

* PostgreSQL integration using psycopg2.
* Dockerized PostgreSQL using Docker Compose.
* Automatic table creation.
* Historical cryptocurrency price storage.
* Timestamped records.
* Database transaction management.
* Automatic cleanup of database resources.
* Context manager support for database connections.

---

## Report Generation

* Generate formatted cryptocurrency reports.
* Display reports in the terminal.
* Save reports as text files.
* Timestamp every generated report.
* Centralized report file configuration.

---

## Email Automation

* SMTP email integration.
* Secure TLS connection.
* Plain text email support.
* Automatic report delivery.
* Report attachment support.
* Configurable sender and receiver.

---

## Scheduling

* Automated execution using Windows Task Scheduler.
* Daily or custom schedules.
* Automatically:

  * Fetches cryptocurrency prices.
  * Updates PostgreSQL.
  * Generates reports.
  * Sends email reports.
  * Logs execution.

---

## Logging

* Centralized logger configuration.
* File logging.
* Console logging.
* INFO, WARNING and ERROR log levels.
* API logging.
* Database logging.
* Email logging.
* Report generation logging.
* Application lifecycle logging.

---

## Configuration

* Environment variables managed using `.env`.
* Example configuration using `.env.example`.
* Centralized configuration using `config.py`.
* Configurable:

  * Database settings
  * Email settings
  * API timeout
  * Retry attempts
  * Report path

---

## Testing

The project includes automated unit tests using **pytest** and **unittest.mock**.

Current test coverage includes:

* Report generation
* CoinGecko API integration
* Database connection
* Database insert operations
* Database retrieval
* API success and failure scenarios
* Email sending
* Database connection failures

Run all tests:

```bash
pytest
```

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
├── tests/
│   ├── test_db.py
│   ├── test_fetch_crypto.py
│   ├── test_report.py
│   └── test_email_sender.py
│
├── reports/
├── logs/
├── docs/
│   └── windows_task_scheduler.md
│
├── requirements.txt
├── pytest.ini
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# Technologies Used

* Python 3
* Requests
* PostgreSQL
* psycopg2
* Docker
* Docker Compose
* python-dotenv
* smtplib
* EmailMessage
* Python Logging
* pytest
* unittest.mock
* Windows Task Scheduler

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
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=crypto_tracker

# API Configuration
REQUEST_TIMEOUT=10
MAX_RETRIES=3

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver@gmail.com
```

---

# Docker Setup

Start PostgreSQL:

```bash
docker compose up -d
```

Verify container:

```bash
docker ps
```

Stop PostgreSQL:

```bash
docker compose down
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd multi-crypto-price-tracker
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file from `.env.example`.

Start PostgreSQL:

```bash
docker compose up -d
```

Run the application:

```bash
python main.py
```

Run tests:

```bash
pytest
```

---

# Scheduling

The project supports automated execution using **Windows Task Scheduler**.

Each scheduled execution:

1. Fetches cryptocurrency prices.
2. Stores prices in PostgreSQL.
3. Generates a report.
4. Saves the report.
5. Sends the report by email.
6. Logs the entire execution.

Documentation:

```text
docs/windows_task_scheduler.md
```

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

Report:

```text
reports/crypto_report.txt
```

Logs:

```text
logs/app.log
```

---

# Error Handling

## API

* Timeout handling
* Connection failures
* HTTP status validation
* JSON validation
* Retry mechanism
* Exponential backoff
* Missing data validation

## Database

* Connection failures
* SQL execution errors
* Transaction management
* Automatic resource cleanup

## Email

* SMTP connection failures
* Authentication failures
* Attachment handling
* Email sending failures

## Logging

* File logging
* Console logging
* Warning tracking
* Error tracking
* Application lifecycle monitoring

---

# Production Improvements

This project follows several production-style backend practices:

* Modular project architecture
* Environment-based configuration
* Configuration validation
* Configurable retry settings
* Configurable request timeout
* Context managers
* Centralized logging
* Dual log handlers (console + file)
* Type hints
* Reusable helper functions
* Centralized report path configuration
* Database transaction safety
* Automatic resource cleanup
* Unit testing using pytest
* Mocking external services with unittest.mock

---

# Learning Outcomes

This project was built to practice:

* REST API integration
* PostgreSQL
* Docker
* Retry and resilience patterns
* SMTP email automation
* Windows Task Scheduler
* Logging
* Environment variable management
* Context managers
* Type hints
* pytest
* Mocking external dependencies
* Backend application architecture
* Production-ready Python development

---

# Future Improvements

* CSV export
* Excel export
* HTML email reports
* Summary statistics
* Streamlit dashboard
* Dockerize the Python application
* GitHub Actions CI/CD pipeline
* Linux cron scheduling
* Integration tests
* Test coverage reporting
