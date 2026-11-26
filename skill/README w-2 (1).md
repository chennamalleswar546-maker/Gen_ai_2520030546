# LLM Client - Gemini and Ollama

This is a small Python project where we can use an LLM from either Gemini or Ollama.

The main idea is simple: the user chooses which provider to use, enters a question, and the program sends that question to the selected model and prints the answer.

## What it can do

- Use Gemini as the cloud LLM
- Use Ollama as a local LLM
- Switch between the two providers from the terminal
- Handle some common connection/API errors
- Retry Gemini when there is a temporary server problem
- Run a small test for the common LLM client

## Project files

```text
project-folder/
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### main.py

This is the file we run. It asks us to choose Gemini or Ollama and then takes the question from the user.

### llm_client.py

This file contains the main LLM classes.

There is a common `LLMProvider` interface, and then separate providers for Gemini and Ollama. This makes it possible to change the provider without changing the main client code.

### test_client.py

This contains a simple test for the `LLMClient`. It uses a fake provider so the test does not need to connect to Gemini or Ollama.

### requirements.txt

The project uses these Python packages:

```text
python-dotenv
pytest
google-genai
requests
```

Install them with:

```bash
pip install -r requirements.txt
```

## Setting up the project

First, make sure Python is installed.

Then create a virtual environment if you want:

```bash
python -m venv .venv
```

On Ubuntu/Linux:

```bash
source .venv/bin/activate
```

Now install the packages:

```bash
pip install -r requirements.txt
```

## Using Gemini

For Gemini, add your API key to the `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Keep the API key private and don't upload the `.env` file to GitHub.

Then run:

```bash
python main.py
```

Choose:

```text
gemini
```

Then enter your question.

## Using Ollama

First make sure Ollama is installed and running on your computer.

The project uses the `llama3.2` model by default.

Run:

```bash
python main.py
```

When it asks for the provider, enter:

```text
ollama
```

Then type your question.

Ollama is accessed through the local API at:

```text
http://localhost:11434/api/generate
```

## Example

When the program starts, it asks:

```text
Choose provider (gemini/ollama):
```

After selecting a provider:

```text
Enter your question:
```

For example:

```text
Explain Artificial Intelligence in simple words.
```

The answer will then be printed as:

```text
LLM Response:
[model response]
```

## Testing

The project has a basic unit test for the common client.

Run:

```bash
python -m unittest test_client.py
```

The test uses a fake provider and checks whether the response is returned correctly.

## Error handling

The program gives an error if the Gemini API key is missing or if an invalid provider is selected.

For Gemini, temporary server problems are retried automatically.

For Ollama, the program shows an error if it cannot connect to the local Ollama server.

## Why both Gemini and Ollama?

Gemini is useful when we want to use a cloud-based model through an API.

Ollama is useful when we want to run a model locally.

Keeping both options in the same project makes it easier to switch between them.

## Future improvements

Some things that can be added later:

- Add more LLM providers
- Keep a conversation history
- Add a proper chat loop
- Let the user select different Ollama models
- Add more unit tests
- Create a simple web interface
