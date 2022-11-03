class Graph(dict):
  def __init__(self, vertex_list, edge_list):
    for v in vertex_list:
      self[v] = set()
    for e in edge_list:
      self.add_edge(e)

  def add_edge(self, edge):
    if len(self[edge[0]]) <= 50 and len(self[edge[1]]) <= 50:
      self[edge[0]].add(edge[1])
      self[edge[1]].add(edge[0])
    else:
      return "This vertex has reach the limit number of edges"

  def add_vertex(self, vertex):
    self[vertex] = set()

  def delete_edge(self, edge):
    self[edge[0]].remove(edge[1])
    self[edge[1]].remove(edge[0])

  def delete_vertex(self, vertex):
    temp_neighbour_set = self[vertex].copy()
    for neighbour_vertex in temp_neighbour_set:
      self.delete_edge((neighbour_vertex, vertex))
    del self[vertex]
  
  def no_edges(self):
    for i in self:
      temp = self[i].copy()
      for neighbour_vertex in temp:
        self.delete_edge((neighbour_vertex, i))
  
  def isEulerian(self):
    odd = 0
    for i in self:
      temp = self[i].copy()
      if len(temp) % 2 != 0:
        odd+=1
    
    if odd == 0:
      return "Has eulerian circuit"
    else:
      return "Don't have eulerian circuit"