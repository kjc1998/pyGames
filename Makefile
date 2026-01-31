PYTHON := python
PIP := pip

#' package: build package
package:
	$(PIP) install --upgrade pip build
	$(PYTHON) -m build

#' install: install package
install: package
	$(PIP) install $(shell echo dist/*.whl)

#' devinstall: install package in development mode
devinstall:
	$(PIP) install -e ".[dev]"

#' check: run typecheck and formatcheck
check: typecheck formatcheck
	@echo "✅ All checks passed!"

#' tests: alias for test
tests: test

#' test: unit tests + type checking
test: typecheck

#` unittest: run unit tests
unittest:
	pytest --verbose tests

#' typecheck: check type annotations
typecheck:
	mypy --strict src
	pytest --mypy --verbose tests

#' formatcheck: run formatter check
formatcheck:
	black --check src tests

#' clean: remove all build, test, coverage and Python artifacts
clean: clean-build clean-pyc clean-test

#' clean-build: remove build artifacts'
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr $(VERSION_FILE)
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

#' clean-pyc: remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

#' clean-test: remove test and coverage artifacts
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr .mypy_cache

.PHONY: package install devinstall check tests test unittest typecheck formatcheck clean clean-build clean-pyc clean-test
