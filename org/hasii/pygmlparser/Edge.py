
from typing import cast


class Edge:
    def __init__(self):

        # mandatory attributes id, source, and target from GML
        self.id:     int = cast(int, None)
        self.source: int = cast(int, None)
        self.target: int = cast(int, None)

        self.label: int = ''
        self.source_node = None
        self.target_node = None

    def __str__(self):
        return 'edge [\n{}\n]'.format('\n'.join(
            map(lambda x: '  {} {}'.format(x, repr(getattr(self, x)).replace("'", '"')),
                filter(lambda x: '_' not in x, dir(self)))))

    def __repr__(self):
        return self.__str__()
