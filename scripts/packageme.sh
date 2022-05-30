#!/usr/bin/env bash

clear

rm -rf dist build
rm -rf PyGMLParser.egg-info
# python3 setup.py sdist bdist_wheel
python3 -m build --sdist --wheel

# Check package
twine check dist/*
