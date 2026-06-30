# Multi Crypto Price Tracker

A Python backend project that fetches real-time cryptocurrency prices from the CoinGecko API, stores them in a PostgreSQL database running inside Docker, generates formatted reports, and logs application activity for monitoring and debugging.

---

## Overview

This project demonstrates how to:

- Consume data from a public REST API.
- Store cryptocurrency prices in PostgreSQL.
- Generate formatted reports from stored data.
- Log application events and errors.
- Manage configuration using environment variables.
- Run PostgreSQL inside Docker.
- Organize Python code into reusable modules.
- Handle database transactions safely.
- Build a modular backend application following production-style practices.

---

## Features

### API Integration

- Fetch real-time cryptocurrency prices from the CoinGecko API.
- Track multiple cryptocurrencies:
  - Bitcoin (BTC)
  - Ethereum (ETH)
  - Solana (SOL)
  - Binance Coin (BNB)
- HTTP request handling using Requests.
- Request timeout support.
- HTTP status validation.
- Safe JSON extraction using `.get()` methods.

### Database Integration

- PostgreSQL integration using psycopg2.
- Dockerized PostgreSQL using Docker Compose.
- Automatic database table creation.
- Historical cryptocurrency price storage.
- Timestamp for every stored record.
- Retrieve historical price data.
- Transaction management using commit and rollback.
- Automatic cleanup of database resources.

### Report Generation

- Generate formatted cryptocurrency price reports.
- Display reports in the terminal.
- Save reports as text files.
- Timestamp every generated report.
- Automatically create readable report output.

### Logging System

- Centralized logging configuration.
- INFO, WARNING and ERROR log levels.
- Database operation logging.
- API request logging.
- Report generation logging.
- Application lifecycle logging.
- Log output stored in `logs/app.log`.

### Configuration Management

- Environment variables managed through `.env`.
- Centralized configuration using `config.py`.
- Safe configuration sharing through `.env.example`.

---

## Project Structure

```text
multi-crypto-price-tracker/
│
├── fetch_crypto.py         # CoinGecko API integration
├── db.py                   # PostgreSQL database operations
├── report.py               # Report generation
├── logger_config.py        # Logging configuration
├── config.py               # Environment configuration
├── main.py                 # Application entry point
│
├── reports/                # Generated reports
├── logs/                   # Application logs
│
├── requirements.txt
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

## Technologies Used

- Python 3
- Requests
- PostgreSQL
- psycopg2
- Docker
- Docker Compose
- python-dotenv
- Python Logging

---

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS multi_crypto_price (
    id SERIAL PRIMARY KEY,
    crypto_name VARCHAR(50) NOT NULL,
    price_usd NUMERIC(18,8) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=crypto_tracker
```

### Example `.env.example`

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=crypto_tracker
```

---

## Docker Setup

### Start PostgreSQL

```bash
docker compose up -d
```

### Verify Container Status

```bash
docker ps
```

### Stop PostgreSQL

```bash
docker compose down
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd multi-crypto-price-tracker
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file using `.env.example`.

### 6. Start PostgreSQL

```bash
docker compose up -d
```

### 7. Run the Application

```bash
python main.py
```

---

## Example Console Report

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

## Generated Files

### Report

```
reports/crypto_report.txt
```

### Logs

```
logs/app.log
```

Example log output:

```text
2026-06-30 18:20:51 - INFO - Application started
2026-06-30 18:20:52 - INFO - Successfully fetched cryptocurrency prices
2026-06-30 18:20:52 - INFO - Creating database table
2026-06-30 18:20:52 - INFO - Successfully inserted bitcoin price
2026-06-30 18:20:53 - INFO - Report generated successfully
2026-06-30 18:20:53 - INFO - Application finished execution
```

---

## Error Handling

### API Errors

- Connection errors
- Timeout errors
- HTTP status validation
- Safe JSON extraction

### Database Errors

- Connection failures
- SQL execution errors
- Transaction rollback
- Automatic resource cleanup

### Logging

- Application events
- Database operations
- Report generation
- Error tracking
- Warning messages

---

## Learning Outcomes

This project was built to practice:

- REST API integration
- JSON data processing
- PostgreSQL database operations
- Docker fundamentals
- Environment variable management
- Python modular programming
- Report generation
- Application logging
- Database transaction handling
- Error handling
- Backend project architecture

---

## Future Improvements

Planned enhancements include:

- Retry and fallback mechanisms
- Email report automation
- Scheduled daily execution
- CSV and Excel export
- Summary statistics
- Interactive dashboard (Streamlit)
- Dockerized application deployment
- Unit and integration tests
- CI/CD pipeline using GitHub Actions