# Token Economics & Budget Calculator

This is a small Python project for checking the estimated token usage, API cost, rate limits, and budget for an LLM feature.

The program takes the expected usage details from environment variables and gives a simple report showing whether the planned usage is within the configured limits.

## What this project does

The calculator checks:

- Input tokens used per day
- Output tokens used per day
- Total tokens per day
- Estimated daily cost
- Estimated monthly cost
- Peak requests per minute (RPM)
- Peak tokens per minute (TPM)
- Daily budget
- Monthly budget
- Safety margin

A 30-day month is used for the monthly cost calculation.

## Files

### `budget.py`

Main program.

It contains the `FeatureBudget` class, which reads the configuration and performs the calculations. It also prints a final report with `PASS` or `REVIEW` for each check.

### `test_budget.py`

Contains unit tests for the budget calculations.

The tests check things like:

- Cost calculation
- RPM and TPM limits
- RPM failure case
- Monthly budget failure case

### `requirements(5).txt`

Contains the Python dependency:

```text
python-dotenv
```

## How the calculation works

The program first calculates the number of input and output tokens used in one day.

```text
Input tokens/day = requests/day × average input tokens
Output tokens/day = requests/day × average output tokens
```

Then it calculates the estimated API cost using the input and output prices per million tokens.

A safety margin is also added when checking the peak RPM, TPM, and budget limits.

## Setup

Make sure Python is installed.

Install the required package:

```bash
pip install -r requirements(5).txt
```

The project uses `python-dotenv` to load values from environment variables.

## Environment variables

The program expects these values:

```text
REQUESTS_PER_DAY
AVG_INPUT_TOKENS
AVG_OUTPUT_TOKENS
PEAK_REQUESTS_PER_MINUTE
INPUT_PRICE_PER_MILLION
OUTPUT_PRICE_PER_MILLION
RPM_LIMIT
TPM_LIMIT
MONTHLY_BUDGET_USD
DAILY_BUDGET_USD
SAFETY_MARGIN_PERCENT
```

Example `.env`:

```env
REQUESTS_PER_DAY=1000
AVG_INPUT_TOKENS=1000
AVG_OUTPUT_TOKENS=500
PEAK_REQUESTS_PER_MINUTE=10

INPUT_PRICE_PER_MILLION=1.0
OUTPUT_PRICE_PER_MILLION=2.0

RPM_LIMIT=100
TPM_LIMIT=50000

MONTHLY_BUDGET_USD=100
DAILY_BUDGET_USD=5

SAFETY_MARGIN_PERCENT=20
```

## Run the project

Run:

```bash
python budget.py
```

You will get a report similar to:

```text
TOKEN ECONOMICS REPORT
-----------------------------------
Input tokens/day:  1,000,000
Output tokens/day: 500,000
Total tokens/day:  1,500,000
Estimated daily cost:   $2.0000
Estimated monthly cost: $60.00
Peak RPM with margin: 12.0
Peak TPM with margin: 18000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: PASS

Recommendation: WITHIN configured planning limits.
```

The exact output depends on the values in the `.env` file.

## Run tests

To run the tests:

```bash
python -m unittest test_budget.py
```

The test file uses sample values such as 1000 requests per day, 1000 input tokens, and 500 output tokens per request.

## Validation

The program also checks for invalid negative usage assumptions and negative safety margins. If these values are negative, it raises a `ValueError`.

## In simple words

This project helps answer:

> "If we build this LLM feature, how many tokens will it use, how much will it cost, and will it stay inside our API and budget limits?"

It can be useful before building or deploying an LLM-based feature because the expected usage can be checked first.

## Future improvements

Some possible improvements are:

- Add a simple user interface
- Support different models and prices
- Export the report to CSV or JSON
- Add graphs for daily and monthly costs
- Add more test cases
