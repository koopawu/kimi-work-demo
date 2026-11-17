# Contributing

Thank you for contributing to kimi-work-demo.

## Development setup

1. Fork the repository and create a feature branch from `main`.
2. Create a virtual environment with Python 3.10 or newer.
3. Install the project in editable mode:

   ```bash
   python -m pip install -e .
   ```

4. Run the test suite before submitting your changes:

   ```bash
   python -m unittest discover -s tests -v
   ```

## Code style

- Follow PEP 8 and keep public functions documented.
- Add type hints to new functions.
- Add or update tests for behavior changes.
- Keep changes focused and avoid unrelated formatting edits.

## Commits and pull requests

- Use [Conventional Commits](https://www.conventionalcommits.org/), for example `feat: add greeting templates` or `fix: handle blank names`.
- Describe the motivation and testing performed in the pull request.
- Run all tests before requesting review.
