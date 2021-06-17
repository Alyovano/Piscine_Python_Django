#!/bin/sh

echo "Version de PIP"
pip --version
pip3 install --upgrade --ignore-installed --target=local_lib$PWD pip install git+https://github.com/jaraco/path.git >> file.log
python3 my_program.py