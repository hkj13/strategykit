# Contributing to StrategyKit

Thank you for your interest in contributing! 

## Development Setup

```bash
git clone https://github.com/yourusername/strategykit.git
cd strategykit
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest
pytest --cov=strategykit
```

## Code Style

We use `black` for formatting and `ruff` for linting:

```bash
black src tests
ruff check src tests
```

## Adding New Frameworks

1. Create new module in `src/strategykit/`
2. Add comprehensive docstrings
3. Write tests in `tests/`
4. Update `__init__.py` and README
5. Add example in `examples/`

## Pull Request Process

1. Fork the repository
2. Create feature branch
3. Write tests for new features
4. Ensure all tests pass
5. Submit PR with clear description

## Questions?

Open an issue or reach out to maintainers.
