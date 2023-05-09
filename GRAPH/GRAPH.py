
def BFS(_grapf, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while queue:
        vertex = queue.pop(0)
        nodes = _grapf[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        # print('queue', queue)
        print('vertex', vertex)


def DFS(_graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while stack:
        vertex = stack.pop()
        nodes = _graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        # print('stack', stack)
        print('vertex', vertex)


class Graph:
    def __init__(self, _graph=None):
        if _graph is None:
            _graph = {}
        self.__graph = _graph

    def showGraph(self):
        for g in self.__graph:
            print(g, self.__graph[g])

    def getVertices(self):
        return list(self.__graph)

    def getEdges(self):
        edge = []
        for vertice in self.__graph:
            for sub_vertice in self.__graph[vertice]:
                path = {vertice, sub_vertice}
                if path not in edge:
                    edge.append(path)
        return edge

    def addVertice(self, _vertice):
        if _vertice not in self.__graph:
            self.__graph[_vertice] = []

    def addEdge(self, _edge):
        _vertice1, _vertice2 = _edge
        if _vertice1 in self.__graph:
            self.__graph[_vertice1].append(_vertice2)
        if _vertice2 in self.__graph:
            self.__graph[_vertice2].append(_vertice1)

    def deleteVertice(self, _vertice):
        if _vertice not in self.__graph:
            return

        _node = self.__graph[_vertice]
        for n in _node:
            self.__graph[n].remove(_vertice)
        self.__graph.pop(_vertice)


if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }

    print('--- BFS ---')
    BFS(graph, 'E')

    print('--- DFS ---')
    DFS(graph, 'E')

    g = Graph(graph)
    g.addVertice('G')
    g.addEdge({'F', 'G'})
    g.addEdge({'D', 'G'})
    g.deleteVertice('F')
    print('--- show vertices ---')
    print(g.getVertices())
    print('--- show edges ---')
    print(g.getEdges())
    print('--- show graph ---')
    g.showGraph()
