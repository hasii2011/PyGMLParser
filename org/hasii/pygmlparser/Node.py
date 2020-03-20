
from typing import cast

from org.hasii.gmlparser.graphics.NodeGraphics import NodeGraphics


class Node:
    def __init__(self):
        # must have attribute id from GML
        self.graphics: NodeGraphics = NodeGraphics()

        self.id: int = cast(int, None)
        self.is_anon = False
        self.forward_edges  = []  # edges where this node is source
        self.backward_edges = []  # edges where this node is target

    def __str__(self):
        return 'node [\n{}\n]'.format('\n'.join(
            map(lambda x: '  {} {}'.format(x, repr(getattr(self, x)).replace("'", '"')),
                filter(lambda x: x in ('is_anon',) or '_' not in x, dir(self)))))

    def __repr__(self):
        return self.__str__()
