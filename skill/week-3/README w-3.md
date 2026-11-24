# LLM Monitoring Project

This project is a small LLM client that can work with both Gemini and Ollama.

The main part is pretty simple: choose Gemini or Ollama, enter a question, and get the answer in the terminal. Along with the answer, the project also keeps track of things like token usage, response time, and estimated cost.

The usage details are stored in MongoDB.

## What this project does

- Connects to Gemini or local Ollama
- Takes a question from the terminal
- Generates an answer from the selected model
- Counts input and output tokens
- Measures how long the request takes
- Calculates an estimated Gemini API cost
- Stores usage details in MongoDB
- Retries some temporary errors
- Has a basic test for the LLM client

## Files

```text
project-folder/
│
├── main.py
├── llm_client.py
├── usage_logger.py
├── test_client.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### main.py

This is the file we run.

It asks whether we want to use Gemini or Ollama and then takes the question from the user. After getting the response, it prints the answer and closes the MongoDB connection.

### llm_client.py

This file handles the LLM providers.

There are two options:

- Gemini - uses the Gemini API
- Ollama - uses the local Ollama API

It also keeps track of the input tokens, output tokens, total tokens, response time, and estimated cost.

### usage_logger.py

This file handles MongoDB.

After an LLM request, the usage information is saved in the `llm_monitoring` database under the `api_usage` collection.

### test_client.py

This contains a simple unit test for the LLM client.

It uses a fake provider and fake logger, so the test does not need to call Gemini or MongoDB.

### requirements.txt

The project needs these packages:

```text
python-dotenv
google-genai
requests
pymongo
pytest
```

Install them with:

```bash
pip install -r requirements.txt
```

## Setup

First, make sure Python is installed.

You can create a virtual environment:

```bash
python -m venv .venv
```

For Ubuntu/Linux:

```bash
source .venv/bin/activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

## Environment file

Create a `.env` file and add the required settings.

For example:

```env
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=your_mongodb_connection_string

GEMINI_INPUT_PRICE_PER_MILLION=0
GEMINI_OUTPUT_PRICE_PER_MILLION=0
```

Keep the `.env` file private. It should not be uploaded to GitHub.

## Running the project

Run:

```bash
python main.py
```

The program will ask:

```text
Choose provider (gemini/ollama):
```

Enter either:

```text
gemini
```

or:

```text
ollama
```

Then enter your question.

Example:

```text
Enter your question: Explain Artificial Intelligence in simple words.
```

The response will be printed in the terminal.

You will also see information such as:

```text
Latency: ...
Input tokens: ...
Output tokens: ...
Estimated cost (USD): ...
```

## Gemini

For Gemini, the API key is read from the `.env` file.

The project uses the `gemini-3.5-flash-lite` model by default.

If the Gemini request works, the response and usage details are recorded.

## Ollama

Ollama runs locally on the computer.

The project uses the `llama3.2` model by default and connects to:

```text
http://localhost:11434/api/generate
```

Make sure Ollama is running before selecting `ollama`.

Since Ollama is running locally, the project does not add a hosted API cost for it.

## MongoDB usage logging

The project stores request information in MongoDB.

The database used is:

```text
llm_monitoring
```

and the collection is:

```text
api_usage
```

For each request, the project can store details such as:

- Provider
- Model
- Input tokens
- Output tokens
- Total tokens
- Latency
- Estimated cost
- Request status
- Number of attempts
- Error information when a request fails
- Timestamp

## Retry handling

The LLM client retries requests when it gets some temporary problems such as timeouts, connection errors, rate limits, or server errors.

It can try the request up to three times, with a short delay between attempts.

## Testing

Run the unit test with:

```bash
python -m unittest test_client.py
```

The test checks that the LLM client returns the expected answer and records the token information correctly.

## Common problems

### Gemini API key error

Check that `GEMINI_API_KEY` is present in `.env`.

### Ollama connection error

Make sure Ollama is running and that the `llama3.2` model is available.

### MongoDB connection error

Check the `MONGODB_URI` in `.env` and make sure the MongoDB server is reachable.

## Future improvements

Some things that can be added later:

- Add a proper chat history
- Create a dashboard for the MongoDB usage data
- Add more LLM providers
- Add more detailed cost tracking
- Export usage reports
- Add more tests
- Add a simple web interface
