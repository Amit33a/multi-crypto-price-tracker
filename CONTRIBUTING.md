# Contributing

Thank you for your interest in contributing to this project.

## Prerequisites

- Python 3.14+
- Docker Desktop
- PostgreSQL (via Docker Compose)
- Git

## Setup

Clone the repository:

```bash
git clone <repository-url>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`.

Start PostgreSQL:

```bash
docker compose up -d
```

Run the application:

```bash
python main.py
```

Run the tests:

```bash
pytest
```

## Coding Guidelines

- Follow PEP 8.
- Write meaningful commit messages.
- Add tests for new functionality whenever possible.
- Keep functions small and focused.