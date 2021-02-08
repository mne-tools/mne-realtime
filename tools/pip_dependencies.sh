#!/bin/bash -ef

python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python -m pip install numpy scipy matplotlib
python -m pip install -r requirements.txt
python -m pip install https://github.com/mne-tools/mne-python/archive/c304072d1c67912da9b4ac62fe64e07ed41f2dd6.tar.gz
python -m pip install -ve .
