#!/usr/bin/env bash

clear

twine upload --repository-url https://test.pypi.org/legacy/ dist/*
