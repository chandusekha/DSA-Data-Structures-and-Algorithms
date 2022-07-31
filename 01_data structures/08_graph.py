class Graph:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v2].remove(v1)
                self.adj_list[v1].remove(v2)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,v1):
        if v1 in self.adj_list.keys():
            for i in self.adj_list[v1]:
                self.adj_list[i].remove(v1) 
            del self.adj_list[v1]
            return True
        return False


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ' : ',self.adj_list[vertex])

g1=Graph()
print(g1.add_vertex('A'))
print(g1.add_vertex('B'))
print(g1.add_vertex('C'))
print(g1.add_vertex('D'))


g1.print_graph()

print(g1.add_edge('A','B'))
print(g1.add_edge('A','C'))
print(g1.add_edge('D','C'))
print(g1.add_edge('D','B'))
print(g1.add_edge('D','A'))
# print(g1.remove_edge('C','B'))
# print(g1.add_edge('c'))

g1.print_graph()
g1.remove_vertex('D')
g1.print_graph()
