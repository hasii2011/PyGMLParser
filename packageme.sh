#!/bin/bash

clear

rm -rf dist build
python3 setup.py sdist bdist_wheel

# Check package
twine check dist/*
