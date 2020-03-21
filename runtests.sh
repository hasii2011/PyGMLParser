#!/bin/bash

clear

cd tests

pytest TestEdge.py TestNode.py TestGraph.py TestParser.py

status=$?
echo "Exit with status: ${status}"
exit ${status}
