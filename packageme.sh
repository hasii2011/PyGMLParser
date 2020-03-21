#!/bin/bash

clear

rm -rf dist build
rm -rf PyGMLParser.egg-info
python3 setup.py sdist bdist_wheel

# Check package
twine check dist/*
