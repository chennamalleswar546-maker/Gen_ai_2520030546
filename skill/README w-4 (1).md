# Tokenizer Comparison

This is a small Python project to compare how different tokenizers break the same text into tokens.

The program uses three tokenizers and checks them with English, Telugu, and Hindi text. It prints the tokens, token IDs, and total number of tokens for each one.

## What this project does

The project compares:

- BPE - GPT-2
- WordPiece - Multilingual BERT
- SentencePiece - XLM-R

The same three sentences are given to each tokenizer:

```text
English: Artificial intelligence is changing the world.

Telugu: కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.

Hindi: कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।
```

The program then shows how each tokenizer handles the text.

## Files

```text
project-folder/
├── tokenizer_comparison.py
├── requirements.txt
└── README.md
```

### tokenizer_comparison.py

This is the main Python file.

It loads the three tokenizers, processes the English, Telugu, and Hindi text, and prints the results.

For each input, it shows:

- Tokens
- Token IDs
- Token count

### requirements.txt

The project uses:

```text
transformers
sentencepiece
```

These are needed to load and use the tokenizers.

## Setup

Make sure Python is installed.

You can create a virtual environment if needed:

```bash
python -m venv .venv
```

On Ubuntu/Linux:

```bash
source .venv/bin/activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

## Run the project

Run:

```bash
python tokenizer_comparison.py
```

The program will first load the tokenizers.

After that, it will print the results for each language.

The output will look roughly like:

```text
===========================================================================
LANGUAGE: English
INPUT TEXT: Artificial intelligence is changing the world.
===========================================================================

BPE - GPT-2
Tokens     : [...]
Token IDs  : [...]
Token count: ...

WordPiece - Multilingual BERT
Tokens     : [...]
Token IDs  : [...]
Token count: ...

SentencePiece - XLM-R
Tokens     : [...]
Token IDs  : [...]
Token count: ...
```

The exact tokens and token counts depend on the tokenizer models.

## What we can observe

This project helps us see that different tokenizers can split the same sentence in different ways.

It is especially useful for comparing how English, Telugu, and Hindi are handled by different tokenization methods.

## Tokenizer types used

### BPE

GPT-2 uses Byte Pair Encoding (BPE). It breaks text into smaller pieces based on patterns learned during training.

### WordPiece

Multilingual BERT uses WordPiece tokenization. Words can be split into smaller subword pieces.

### SentencePiece

XLM-R uses SentencePiece. It can work directly with text without depending on spaces in the same way as normal word-based tokenization.

## Notes

The first time the program is run, the tokenizer models may need to be downloaded.

An internet connection may therefore be required for the first run.

After the models are available locally, they can be loaded again without downloading them each time.

## Possible improvements

Some things that can be added later:

- Compare more languages
- Add more tokenizer models
- Save the results to a file
- Create a table comparing token counts
- Add charts for the comparison
