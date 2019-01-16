#V = {a, b, c, d, e}
#E = {ab, ac, bd, cd, de}

# graph = { "a" : ["b","c"],
#           "b" : ["a", "d"],
#           "c" : ["a", "d"],
#           "d" : ["e"],
#           "e" : ["d"]
#          }
#
# #Print the graph
# print(graph)


class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def edges(self):
        return self.findedges()

    def AddEdge(self, edge):
        if isinstance(edge,dict):
            for k,v in edge.items():
                self.addVertex(k)
                for e in v:
                    self.gdict[k].append(e)

    def findedges(self):
        edge_name = []
        for k,v in self.gdict.items():
            for e in v:
                if[e,k] not in edge_name:
                    edge_name.append([k,e])
        return edge_name



graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
g.addVertex("f")
g.AddEdge({'f':['a','b']})
g.AddEdge({'c':['f']})
print(g.getVertices())
print(g.findedges())