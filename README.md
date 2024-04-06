# datasette-import

[![PyPI](https://img.shields.io/pypi/v/datasette-import.svg)](https://pypi.org/project/datasette-import/)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-import?include_prereleases&label=changelog)](https://github.com/datasette/datasette-import/releases)
[![Tests](https://github.com/datasette/datasette-import/actions/workflows/test.yml/badge.svg)](https://github.com/datasette/datasette-import/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-import/blob/main/LICENSE)

Tools for importing data into Datasette

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-import
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-import
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
