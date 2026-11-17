# kimi-work-demo

A minimal Python command-line application that demonstrates a clean project layout and automated tests.

## Features

- Python 3.10+
- `src/` package layout
- Type hints and docstrings
- Standard-library unit tests
- MIT license

## Quick start

Create and activate a virtual environment, then install the project in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Run the CLI:

```bash
kimi-demo --name "Kimi"
# Hello, Kimi!
```

You can also run it as a module:

```bash
python -m kimi_work_demo --name "Kimi"
```

## Run tests

After installing the project, run:

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
.
├── src/kimi_work_demo/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── greeting.py
├── tests/
│   ├── test_cli.py
│   └── test_greeting.py
├── CONTRIBUTING.md
├── LICENSE
└── pyproject.toml
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and commit conventions.

## License

This project is licensed under the [MIT License](LICENSE).
