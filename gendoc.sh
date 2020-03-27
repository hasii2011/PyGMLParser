#!/bin/bash

clear
rm -rf html

pdoc3 --force --html --output-dir docs org/
