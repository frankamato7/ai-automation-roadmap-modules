# Module 3 – APIs, Web Requests, and Python Automation

## Goals
- Understand HTTP requests and web APIs
- Use the `requests` library to retrieve data
- Parse JSON responses
- Begin automating data retrieval processes
- Build small API-powered tools and scripts

## Lessons & Highlights

### Lesson 1 – HTTP + API Basics (11/28/25)
- Made a GET request using the `requests` library
- Parsed JSON from multiple public APIs:
  - GitHub API
  - Cat Facts API
  - CoinGecko Bitcoin price API
  - Open-Meteo weather API
- Extracted specific values from nested JSON
- Built a basic API testing notebook

### Lesson 2 – Weather Dashboard CLI (11/28/25)
- Built a command-line weather tool in Python
- Implemented dynamic city lookup using Open-Meteo geocoding
- Retrieved live weather data via API
- Parsed nested JSON responses
- Formatted output cleanly (temperature, wind speed)
- Included error handling for unknown cities and missing coordinates

### Lesson 3 - Crypto Price Automation Bot (11/30/25)
- Built a CLI crypto price alert bot using Python
- Queried CoinGecko API for real-time cryptocurrency prices
- Supported multiple cryptocurrency symbols dynamically
- Used loops and time delays for continuous monitoring
- Added user-defined alert thresholds
- Logged alerts to a file with timestamps
- Implemented error handling for bad inputs and unavailable coins

### Lesson 4 — Task Scheduling + Daily Email Summary (12/01/25)
- Learned how to use APScheduler for automated tasks
- Created a scheduled job that runs on an interval or cron schedule
- Pulled real API data (Bitcoin price + NYC weather)
- Composed a summary message programmatically
- Sent automated emails using SMTP + env variables
- Handled authentication errors and secure credential storage
- Built a complete daily summary automation script
