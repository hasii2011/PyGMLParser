`PyGMLParser` is a [Graph Modeling Language (GML)](https://en.wikipedia.org/wiki/Graph_Modelling_Language) standalone parser for Python 3.

It is a fork of: [icasdri/gml.py](https://github.com/icasdri/gml.py)

The specific updates are:

* Updated to Python 3
* Use f-strings
* Separate files for each class
* Use packages instead of single file
* Updated GML format from Tulip .gml files to include the following keywords keyword used by the 
[Python Tulip](https://tulip.labri.fr/Documentation/current/tulip-python/html) gml exporter ('GML Export')
    * `graphics`
    * `Line`
    * `point`
* Use dataclasses for graphics and points
* Use type hinting and custom typing for readability and maintainability
* Use Python logging for debugging
* Introduced small unit test

