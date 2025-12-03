# AI Automation Roadmap – What I Learned So Far

## Overview
This repo contains everything I have learned on my AI automation roadmap self-taught journey:
- Following a 10-module AI automation roadmap
- Each module has lessons with code, notebooks, and mini-projects

## Module Index
- [Module 1 – Python Fundamentals](module-01-python-fundamentals/README.md)
- [Module 2 – Intermediate Python + Data Handling](module-02-intermediate-python-data/README.md)
- [Module 3 - APIs, Web Requests, and Python Automation](module-03-apis-automation/README.md)
- [Module 4 - LLM Prompt Engineering](module-04-llm-prompt-engineering/README.md)

## What I Learned So Far

### Python & Core Programming
- Writing and running Python scripts (VS Code + Terminal)
- Variables, user input, casting, arithmetic, conditionals, loops
- Data structures: lists, dicts, sets, tuples
- Functions, modules, imports, basic debugging
- File I/O: read, write, append, existence and size checks 

### NumPy & pandas
- 1D & 2D arrays, shapes, indexing, vectorized math, stats
- Loading CSVs into DataFrames, filtering, sorting, groupby, merges
- Handling missing values, joins, multi-aggregation
- Building a full Data Explorer workflow over a retail dataset 

### SQL & Pipelines
- SELECT, WHERE, ORDER BY, GROUP BY
- INNER JOIN across `sales` and `products`
- Revenue by category, product, and day
- Running SQL inside Python using `pd.read_sql_query`
- Building a SQL → pandas → visualization → CSV pipeline 

### Git & Workflow
- Staging, committing, pushing, rebasing
- Clean repo structure and project-level READMEs
- Organizing by modules and lessons for a long-term learning roadmap 

### APIs & HTTP
- Making HTTP GET requests with Python
- Using the requests library
- Parsing and navigating JSON responses
- Calling multiple public APIs
- Extracting nested dictionaries from real-world API responses
- Built a full CLI weather dashboard using Python
- Used geocoding to convert city names into coordinates dynamically
- Parsed structured JSON from Open-Meteo
- Built CLI tools using `sys.argv`
- Added error handling for invalid input and missing data

### Crypto Price Alert Bot
- Created an automated crypto monitoring script
- Pulled live price data from CoinGecko API
- Implemented multi-coin support (Bitcoin, Ethereum, Solana, etc.)
- Set user-defined alert thresholds
- Added a monitoring loop with timed intervals
- Logged alerts to a local file for tracking
- Added clean error handling for invalid coins or API issues

### Scheduling & Email Automation
- Used APScheduler to run automated Python tasks
- Built a daily summary job combining multiple API calls
- Sent emails programmatically via SMTP
- Used environment variables to store sensitive credentials
- Implemented error handling for authentication and connection failures
- Completed my first end-to-end scheduled automation script

### API Automation Pipeline
- Built a multi-step automation pipeline combining APIs, pandas, CSV generation, and automated email delivery
- Learned how to structure reusable functions for fetching, cleaning, transforming, and saving data
- Used multipart MIME emails to attach generated files
- Reinforced environment variable use for secure credentials
- Completed a portfolio-ready automation project

### LLM Fundamentals
- Learned core prompt engineering levers: role, structure, constraints
- Created a reusable prompt template library
- Built system, task, formatting, and constraint prompts
- Practiced refining prompts for clarity, boundaries, and consistency
- Established structured folders for LLM tooling in the 

(You can compress/trim as you go, but this is a solid starting shape.)

Going forward, at the end of each session we’ll just add/update bullets in these sections rather than maintaining a separate doc.

### OpenAI API + Summarizer Tool
- Installed and configured openai + python-dotenv
- Created .env and secured your Project API Key
- Built and tested a warm-up script (hello_llm.py)
- Created a reusable OpenAI client helper (client.py)
- Implemented your first Python LLM tool (summarizer.py)
- Built a CLI interface to test the tool
- Added robust error handling for quota issues
- Verified end-to-end functional structure of an AI tool