# Multi Crypto Price Tracker

A Python backend project that fetches real-time cryptocurrency prices from the CoinGecko API and stores them in a PostgreSQL database running inside Docker for historical tracking and analysis.

---

## Overview

This project demonstrates how to:

- Consume data from a public REST API.
- Store data in PostgreSQL.
- Manage configuration using environment variables.
- Run PostgreSQL inside Docker.
- Organize Python code into reusable modules.
- Handle database transactions safely.

---

## Features

### API Integration

- Fetch real-time cryptocurrency prices from the CoinGecko API.
- Track multiple cryptocurrencies:
  - Bitcoin (BTC)
  - Ethereum (ETH)
  - Solana (SOL)
  - Binance Coin (BNB)
- HTTP request handling using the Requests library.
- Request timeout support.
- HTTP status validation.
- Safe JSON extraction using `.get()` methods.

### Database Integration

- PostgreSQL integration using psycopg2.
- Dockerized PostgreSQL using Docker Compose.
- Automatic database table creation.
- Historical price storage with timestamps.
- Retrieve previously stored cryptocurrency prices.
- Transaction management using commit and rollback.
- Proper database connection cleanup.

### Configuration Management

- Environment variables managed through `.env`.
- Centralized configuration using `config.py`.
- Safe sharing of project configuration through `.env.example`.

---

## Project Structure

```text
multi-crypto-price-tracker/
│
├── fetch_crypto.py         # CoinGecko API integration
├── db.py                   # PostgreSQL database operations
├── config.py               # Environment configuration
├── main.py                 # Application entry point
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
DB_PORT=5438
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=crypto_tracker
```

### Example `.env.example`

```env
DB_HOST=localhost
DB_PORT=5438
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
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
git clone <your-repository-url>
cd multi-crypto-price-tracker
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

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

## Example Output

```text
[
 (4, 'binancecoin', Decimal('589.05000000'), datetime.datetime(2026, 6, 18, 10, 33, 19, 552033)),
 (3, 'solana', Decimal('71.37000000'), datetime.datetime(2026, 6, 18, 10, 33, 19, 396641)),
 (2, 'ethereum', Decimal('1744.35000000'), datetime.datetime(2026, 6, 18, 10, 33, 19, 249610)),
 (1, 'bitcoin', Decimal('63955.00000000'), datetime.datetime(2026, 6, 18, 10, 33, 19, 138817))
]
```

---

## Error Handling

The project currently includes:

### API Errors

- Network connection errors
- Request timeout errors
- HTTP status validation
- Safe JSON extraction

### Database Errors

- Database connection failures
- SQL execution errors
- Transaction rollback on failed write operations
- Automatic resource cleanup using `finally`

---

## Learning Outcomes

This project was built to practice:

- REST API integration
- Working with JSON data
- PostgreSQL database operations
- Docker fundamentals
- Environment variable management
- Python modularization
- Database transaction handling
- Basic backend application architecture

---

## Future Improvements

Planned enhancements include:

- CSV export functionality
- Logging system
- Automated scheduled execution
- Daily price reports
- Email notifications
- Data analytics and summaries
- Streamlit dashboard
- Containerized application deployment



