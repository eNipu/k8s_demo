#!/bin/bash

# check if python is installed and install it if not installed
if ! [ -x "$(command -v python)" ]; then
  echo 'Error: python is not installed.' >&2
  sudo apt-get install python
fi

# check if pip is installed and install it if not installed
if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  sudo apt-get install python-pip
fi

# create a virtual environment usig venv module
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# check if poetry is installed and install it if not installed
if ! [ -x "$(command -v poetry)" ]; then
  echo 'Error: poetry is not installed.' >&2
  pip install poetry
fi

# install the dependencies
poetry install

#update the dependencies
poetry update

# run the application
poetry run python app.py