# Gemini API Python Project

This is a simple Python project that connects to the Gemini API and shows the response in the terminal.

## What this project does

The program sends a question to Gemini and prints the answer on the screen.

It also:
- Gets the API key from the `.env` file
- Sends a request to Gemini
- Displays the response
- Tries again if there is a temporary API or server error
- Shows basic error messages if something goes wrong

## Project files

```text
project-folder/
├── main.py
├── .env
├── .gitignore
└── README.md
```

### main.py

This is the main file of the project. It contains the code that connects to Gemini and gets the answer.

### .env

This file stores the Gemini API key.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

Keep this file private. Don't share your actual API key or upload it to GitHub.

### .gitignore

This tells Git which files should not be uploaded, such as `.env`, `.venv`, and Python cache files.

## What you need

Before running the project, make sure you have:

- Python 3
- A Gemini API key
- Internet connection
- `python-dotenv`

Install `python-dotenv` using:

```bash
pip install python-dotenv
```

## How to run the project

Open the project folder in the terminal.

If you are using a virtual environment, you can create one with:

```bash
python -m venv .venv
```

For Ubuntu/Linux, activate it using:

```bash
source .venv/bin/activate
```

Then install the required package:

```bash
pip install python-dotenv
```

Make sure your `.env` file has your Gemini API key.

Now run:

```bash
python main.py
```

You should see the program connect to Gemini and print the response.

## Example

The question used in the current program is:

```text
What is Artificial Intelligence? Explain in simple words.
```

The output will look something like:

```text
Connecting to Gemini API...

========== GEMINI RESPONSE ==========

[Gemini response]

=====================================
```

## If you get an error

If the API key is missing, check your `.env` file and make sure the key is written correctly.

If there is a temporary server or rate-limit problem, the program will wait for a short time and try again.

Other connection, timeout, or API response errors are also handled by the program.

## A few things to remember

- Keep your Gemini API key private.
- Don't put the API key directly inside `main.py`.
- Don't upload the `.env` file to a public GitHub repository.
- Make sure your internet connection is working when you run the program.

## Future changes

This project can be improved later by adding things like:

- Taking questions from the user instead of using one fixed question
- Making a simple chat system
- Saving previous responses
- Adding a small web interface
- Letting the user choose the Gemini model

