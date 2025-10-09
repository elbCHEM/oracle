# Oracle
A simple command-line application that answers your questions with a touch of humor and mystery. 

## Features
- Asks the user for questions and provides random answers

## Installation

1. Clone the repository:
	```sh
	git clone https://github.com/elbCHEM/oracle.git
	cd oracle
	```
2. (Optional) Create and activate a virtual environment:
	```sh
	python -m venv .venv
	```
3. Install dependencies:
	```sh
	pip install -r requirements.txt
	```

## Usage

Run the application from the command line:

```sh
python -m oracle
```

You can also set a random seed for reproducible answers:

```sh
python -m oracle --seed 42
```

## Project Structure

```
magic8ball/
├── src/
│   └── oracle/
│       ├── __main__.py
│       ├── flow.py
│       ├── logic.py
│       └── ...
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE).

---

*Ask your question and let the oracle decide your fate!*
