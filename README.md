`PyGMLParser` is a [Graph Modeling Language (GML)](https://en.wikipedia.org/wiki/Graph_Modelling_Language) standalone parser for Python 3.

It is a fork of: [icasdri/gml.py](https://github.com/icasdri/gml.py)

----------
Get it from PyPi by doing:

`pip3 install PyGMLParser`


Uses [Travis CI](https://travis-ci.org/github/hasii2011/PyGMLParser) for continuous  integration.  

The class documentation is [here](https://hasii2011.github.io/PyGMLParser/)

----------

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
* Introduced a set of small unit tests


### The fast and the dirty
```python3
from org.hasii.pygmlparser.Parser import Parser
from org.hasii.pygmlparser.Graph import Graph
from org.hasii.pygmlparser.Edge import Edge
from org.hasii.pygmlparser.Node import Node
from org.hasii.pygmlparser.graphics.NodeGraphics import NodeGraphics
from org.hasii.pygmlparser.graphics.EdgeGraphics import EdgeGraphics
from org.hasii.pygmlparser.graphics.Point import Point




# Instantiate a parser, load a file, and parse it!
parser: Parser = Parser()
parser.load_gml('/path/to/aGraph.gml')
parser.parse()

# Retrieve the graph nodes 
nodes: Graph.Nodes = graph.graphNodes  # a map of id -> Node objects

# Retrieve the graph edges
edges: Graph.Edges = graph.graphEdges  # list of Edge objects

# Directly access the node or edge attributes
node: Node = graph.graphNodes[0]
edge: Edge = graph.graphEdges[0]

node.id      # the id of this node
edge.source  # the source id of this edge

node.is_anon  # whether or not this node actually appeared as a node block
              # in the input GML (or if it was inferred, via edge source/targets)
              # _True_ if inferred, False if actually appeared

node.forward_edges   # List of Edge instances whose source is this node
node.backward_edges  # List of Edge instances whose target is this node

# Special attributes on Edges
edge.source_node  # Node object corresponding to edge.source (which is an id)
edge.target_node  # Node object corresponding to edge.target (which is an id)

# Get the Tulip extensions
edgeGraphics: EdgeGraphics = edge.graphics
nodeGraphics: NodeGraphics = node.graphics

# Get the edge line drawing description
line:  Tuple[Point] = edgeGraphics.line

```

