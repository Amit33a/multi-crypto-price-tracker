# Multi Crypto Price Tracker

A Python backend automation project that fetches real-time cryptocurrency prices from the CoinGecko API, stores them in a PostgreSQL database running inside Docker, generates formatted reports, sends automated email reports, logs application activity, implements retry mechanisms, and supports automated execution using Windows Task Scheduler.

---

# Overview

This project demonstrates how to:

* Consume data from a public REST API.
* Handle temporary API failures using retry logic.
* Validate API responses before processing data.
* Store cryptocurrency prices in PostgreSQL.
* Generate formatted reports.
* Send automated email reports with file attachments.
* Log application events and errors.
* Manage configuration using environment variables.
* Run PostgreSQL inside Docker.
* Automate application execution using Windows Task Scheduler.
* Organize Python code into reusable modules.
* Handle database transactions safely.
* Build a modular backend application following production-style practices.

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
* Request timeout support.
* HTTP status validation.
* Safe JSON extraction using `.get()` methods.
* Automatic retry mechanism for temporary API failures.
* Configurable retry attempts.
* Delay between retry attempts.
* Validation of API responses before processing.
* Detection of incomplete cryptocurrency data.

---

## Database Integration

* PostgreSQL integration using psycopg2.
* Dockerized PostgreSQL using Docker Compose.
* Automatic database table creation.
* Historical cryptocurrency price storage.
* Timestamp for every stored record.
* Retrieve historical price data.
* Transaction management using commit and rollback.
* Automatic cleanup of database resources.

---

## Report Generation

* Generate formatted cryptocurrency price reports.
* Display reports in the terminal.
* Save reports as text files.
* Timestamp every generated report.
* Automatically create readable report output.

---

## Email Automation

* SMTP email integration.
* Secure email authentication using TLS.
* Send automated cryptocurrency reports.
* Send plain text email messages.
* Attach generated report files to emails.
* Configurable sender and receiver through environment variables.

---

## Scheduling

* Automated execution using Windows Task Scheduler.
* Runs without user interaction.
* Automatically fetches the latest cryptocurrency prices.
* Automatically updates the PostgreSQL database.
* Automatically generates reports.
* Automatically emails the generated report.
* Supports daily or custom execution schedules.
* Includes setup documentation for Task Scheduler.

---

## Logging System

* Centralized logging configuration.
* INFO, WARNING and ERROR log levels.
* API request logging.
* Retry attempt logging.
* Database operation logging.
* Report generation logging.
* Email operation logging.
* Application lifecycle logging.
* Log output stored in `logs/app.log`.

---

## Configuration Management

* Environment variables managed through `.env`.
* Centralized configuration using `config.py`.
* Safe configuration sharing through `.env.example`.

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
├── reports/
├── logs/
├── docs/
│   └── windows_task_scheduler.md
│
├── requirements.txt
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
* Python Logging
* smtplib
* EmailMessage
* Windows Task Scheduler
* Time Module

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

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver@gmail.com
```

---

# Example `.env.example`

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=crypto_tracker

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver@gmail.com
```

---

# Docker Setup

## Start PostgreSQL

```bash
docker compose up -d
```

## Verify Container Status

```bash
docker ps
```

## Stop PostgreSQL

```bash
docker compose down
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd multi-crypto-price-tracker
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file using `.env.example`.

## 6. Start PostgreSQL

```bash
docker compose up -d
```

## 7. Run the Application

```bash
python main.py
```

---

# Automating the Application

The project supports automatic execution using **Windows Task Scheduler**.

Once scheduled, each execution will:

1. Fetch cryptocurrency prices from the CoinGecko API.
2. Store the data in PostgreSQL.
3. Generate a formatted report.
4. Save the report to the `reports` directory.
5. Send the report via email.
6. Log the entire execution.

Detailed scheduling instructions are available in:

```text
docs/windows_task_scheduler.md
```

---

# Example Console Report

```text
CRYPTO PRICE REPORT
==============================
Generated at: 2026-06-30 18:20:51

Bitcoin      $63955.00
Ethereum     $1744.35
Solana       $71.37
Binancecoin  $589.05
```

---

# Generated Files

## Report

```text
reports/crypto_report.txt
```

## Logs

```text
logs/app.log
```

---

# Error Handling

## API Errors

* Connection errors
* DNS resolution failures
* Timeout errors
* HTTP status validation
* Safe JSON extraction
* Automatic retry mechanism
* Delay between retry attempts
* Maximum retry limit
* API response validation
* Missing cryptocurrency detection

## Database Errors

* Connection failures
* SQL execution errors
* Transaction rollback
* Automatic resource cleanup

## Email Errors

* SMTP connection failures
* Authentication failures
* Email sending failures
* Attachment handling failures

## Logging

* Application events
* API requests
* Retry attempts
* Database operations
* Report generation
* Email operations
* Error tracking
* Warning messages

---

# Learning Outcomes

This project was built to practice:

* REST API integration
* HTTP request handling
* Retry and resilience patterns
* JSON data processing
* PostgreSQL database operations
* Docker fundamentals
* Environment variable management
* Python modular programming
* Report generation
* SMTP email automation
* Windows Task Scheduler
* File attachment handling
* Application logging
* Database transaction handling
* Error handling
* Backend project architecture

---

# Future Improvements

Planned enhancements include:

* CSV and Excel export
* HTML email reports
* Summary statistics
* Interactive dashboard (Streamlit)
* Dockerized application deployment
* Unit and integration tests
* CI/CD pipeline using GitHub Actions
* Linux cron scheduling
* Containerized application with Docker
