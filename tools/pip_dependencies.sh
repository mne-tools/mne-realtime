#!/bin/bash -ef

python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python -m pip install -r requirements.txt
python -m pip install -ve .
