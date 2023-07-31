#!/bin/bash

DIR="$(pwd)"
ACTIVATE="/venv/bin/activate"

VENV="$DIR$ACTIVATE"

source $VENV
echo "$(pip3 list)"

pip3 install -r requirements.txt

echo "$(pip3 list)"

