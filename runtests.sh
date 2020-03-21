#!/bin/bash

clear

rm -rf .pytest_cache/

cd tests

pytest TestEdge.py TestNode.py TestGraph.py TestParser.py

status=$?

rm -rf .pytest_cache/

echo "Exit with status: ${status}"
exit ${status}
