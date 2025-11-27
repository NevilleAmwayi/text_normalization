Text Normalization Using Finite-State Transducers (FSTs)

This repository contains a complete text normalization system built using Pynini and OpenFST.
The system normalizes cardinal numbers (0–1000) in English (and optionally French) into their written-out verbal forms.
It was developed as part of the Digital Umuganda Text Normalization Challenge.

Project Overview

Text normalization is a critical pre-processing step for NLP tasks such as:

Text-to-Speech (TTS)

Automatic Speech Recognition (ASR)

Large Language Models (LLMs)

This project focuses on the normalization of cardinal numbers inside full sentences.
For example:

Input:  I have 3 dogs and 21 cats.
Output: I have three dogs and twenty-one cats.


The project uses finite-state transducers (FSTs) for their speed, determinism, and linguistic transparency.

📁 Repository Structure
text-normalization-fst/
│
├── src/
│   ├── cardinal_en.py          # English cardinal grammar
│   ├── cardinal_fr.py          # (Optional) French grammar
│   ├── normalizer.py           # Full text normalization pipeline
│   ├── build_far.py            # FAR compiler script
│   └── utilities.py            # Helpers (optional)
│
├── grammars/
│   └── cardinal.far            # Compiled FST archive
│
├── tests/
│   └── unit_tests.py           # HF unit tests
│
├── report.pdf                  # Methodology + results
├── requirements.txt            # Python dependencies
└── README.md

🧠 How It Works
1. FST Grammar Construction

The grammar covers:

Units (zero–nine)

Teens (ten–nineteen)

Tens (twenty, thirty, … ninety)

Compound numbers (twenty-one → ninety-nine)

Hundreds (one hundred → nine hundred ninety-nine)

1000 → "one thousand"

The FST maps digit strings → written-out English.

🛠️ Installation
1. Clone the Repository
git clone https://github.com/yourusername/text-normalization-fst
cd text-normalization-fst

2. Install Requirements
pip install -r requirements.txt

📦 Build the FAR File
python src/build_far.py


This will produce:

grammars/cardinal.far

🧪 Run Unit Tests

This project includes unit tests from the official challenge dataset:

python tests/unit_tests.py

🔧 Normalize a Sentence
Method 1: Run from Python
python -c "from src.normalizer import normalize_sentence; print(normalize_sentence('I have 42 apples'))"

Method 2: Use inside your scripts
from src.normalizer import normalize_sentence

print(normalize_sentence("He bought 1000 books"))


Output:

he bought one thousand books

📊 Performance

Average runtime: ~0.2 ms per normalized number
FST compilation time: ~0.8 seconds (depending on machine)

🧩 Limitations

Only cardinal numbers 0–1000

Hyphenation follows standard English rules

English is fully implemented; French optional

👤 Author

Neville Shem Amwayi
