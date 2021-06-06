#!/bin/bash
brew install python3
pip3 install venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install poetry
poetry install
