# Windows Task Scheduler Setup

This guide explains how to automatically run the **Multi Crypto Price Tracker** using **Windows Task Scheduler**.

---

# Prerequisites

Before scheduling the application, make sure the following requirements are met:

* Python is installed.
* The project dependencies are installed.
* PostgreSQL Docker container is running.
* The `.env` file is configured correctly.
* Email credentials are valid.
* The project runs successfully using:

```bash
python main.py
```

---

# Create a New Scheduled Task

1. Open **Task Scheduler**.
2. Select **Create Basic Task...**
3. Enter a task name.

Example:

```
Multi Crypto Price Tracker
```

4. Click **Next**.

---

# Configure the Trigger

Choose how often the application should run.

Examples:

* Daily
* Weekly
* Monthly

For testing, you can temporarily choose a frequent schedule.

---

# Configure the Action

Select:

```
Start a program
```

Program/script:

```
python
```

or provide the full path to your Python executable.

Example:

```
C:\Users\<username>\AppData\Local\Programs\Python\Python313\python.exe
```

---

# Add Arguments

Enter the path to your application's entry point.

Example:

```
main.py
```

or

```
C:\Projects\multi-crypto-price-tracker\main.py
```

---

# Start In

Specify the project folder.

Example:

```
C:\Projects\multi-crypto-price-tracker
```

This ensures that relative paths such as:

* reports/
* logs/
* .env

are found correctly.

---

# Finish

Review the configuration and click **Finish**.

---

# Test the Task

Right-click the scheduled task and select:

```
Run
```

Verify that:

* Cryptocurrency prices are fetched.
* Data is inserted into PostgreSQL.
* The report is generated.
* The report is emailed successfully.
* Logs are written to:

```
logs/app.log
```

---

# Verify Database

Open PostgreSQL and confirm that new rows have been inserted into:

```
multi_crypto_price
```

---

# Verify Report

Confirm that the following file has been updated:

```
reports/crypto_report.txt
```

---

# Verify Email

Check the recipient inbox to ensure the report email was delivered successfully.

---

# Verify Logs

Open:

```
logs/app.log
```

A successful execution should contain messages similar to:

```
Application started
API request to CoinGecko
Successfully fetched cryptocurrency prices
Creating database table
Successfully inserted bitcoin price
Generating report
Email sent successfully
Application finished execution
```

---

# Troubleshooting

## Python not found

Ensure the correct Python executable is selected in **Program/script**.

---

## Database connection failed

Verify:

* Docker container is running.
* PostgreSQL is accepting connections.
* Environment variables are correct.

---

## Email not sent

Verify:

* SMTP settings.
* Email username.
* App password.
* Internet connection.

---

## Report not generated

Verify that:

* The `reports` directory exists.
* The application has permission to write files.

---

## Logs not created

Verify that:

* The `logs` directory exists.
* The application has write permission.

---

# Expected Workflow

Each scheduled execution performs the following steps automatically:

1. Start the application.
2. Connect to PostgreSQL.
3. Create the database table if required.
4. Fetch cryptocurrency prices from the CoinGecko API.
5. Retry API requests if temporary failures occur.
6. Validate the API response.
7. Store cryptocurrency prices in PostgreSQL.
8. Generate a formatted report.
9. Save the report to a text file.
10. Send the report by email.
11. Write application logs.
12. Exit successfully.

No user interaction is required after the task has been configured.
