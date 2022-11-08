#!/bin/bash

# This script formats the code in the current directory.
echo "Checking code quality with flake8..."
poetry run flake8 .

echo "Formatting code with black..."
poetry run black .

echo "Formatting code with isort..."
poetry run isort . --profile black

echo "Checking code to find common security..."
poetry run bandit .

echo "Checking code to find common security db from safety check..."
poetry run safety check