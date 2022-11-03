# Classe Base 
class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.adj_list = {}
    for i in vertices:
      self.adj_list[i] = LinkedList()

  def add_edge(self, from_node, to_node):
    self.adj_list[from_node].insert_at_tail(to_node)
    self.adj_list[to_node].insert_at_tail(from_node)



# Funções Base
def delete_edge(graph, start, end):
  if start == end:
    return
  current_node = graph.adj_list[start].head
  previous_node = None
  while current_node:
    if current_node.val == end:
      if previous_node is None:
        graph.adj_list[start].head = current_node.next
        current_node.next = None
        delete_edge(graph, end, start)
      else:
        previous_node.next = current_node.next
        current_node.next = None
        delete_edge(graph, end, start)
      return
    previous_node = current_node
    current_node = current_node.next
    return

def delete_vertex(graph, vertex):
  current_node = graph.adj_list[vertex].head
  edges =  []
  while current_node:
    edges.append(current_node)
    current_node = current_node.next

  for i in edges:
    delete_edge(graph, vertex, i.val)
  
  graph.vertices.remove(vertex)

  return 

def no_edges_graph(graph):
  for i in graph.vertices:
      temp = graph.adj_list[i].get_head()
      while temp is not None:
        delete_edge(graph, i, temp.val)
        temp = temp.next
  return

def isEulerian(graph):
  odd = 0
  for i in graph.vertices:
      count = 0
      temp = graph.adj_list[i].get_head()
      while temp is not None:
        count+=1
        temp = temp.next
      if count % 2 != 0:
        odd += 1

  if odd == 0:
    return "Has eulerian circuit"
  else:
    return "Don't have eulerian circuit"






# Caso 1 -> Próximo e Início
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_tail(self, val):
    if self.is_empty():
      self.head = Node(val)
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = Node(val)
    return

  def get_head(self):
    return self.head

  def is_empty(self):
    return self.head is None





# Caso 2 -> Próximo, Início e Fim
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_at_tail(self, val):
    if self.is_empty():
      self.head = Node(val)
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = Node(val)
    self.tail =  temp.next
    return self.tail

  def get_head(self):
    return self.head

  def get_tail(self):
    return self.tail

  def is_empty(self):
    return self.head is None






# Caso 3 -> Próximo, Anterior, Fim e Início
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_at_tail(self, val):
    if self.is_empty():
      self.head = Node(val)
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = Node(val)
    self.tail =  temp.next
    temp.next.prev = temp
    return self.tail

  def get_head(self):
    return self.head

  def get_tail(self):
    return self.tail

  def is_empty(self):
    return self.head is None
