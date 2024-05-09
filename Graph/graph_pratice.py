# graph

class Graph:
  def __init__(self,edge):
    self.edges=edge
    self.dict={}
    for start,end in self.edges:
      # print(f"{start}:{end}")'
      if start in self.dict:
        self.dict[start].append(end)
      else:
        self.dict[start]=[end]
    # print(self.dict)

  def find_all_paths(self,start,end,path=[]):

    path=path+[start]
    
    if start==end:
      return [path]
    
    if start not in self.dict:
      return
    
    
      # pune 
    for nodes in self.dict[start]:
      # print(nodes)
      new_paths=self.find_all_paths(nodes,end,path)
      print(new_paths)
  


  
objects=[ ("mumbai","pune"),
    ("mumbai","kholapur"),
    ("pune","solapur"),
    ("kholapur","solapur")]

g=Graph(objects)
start="mumbai"
end="solapur"
a=g.find_all_paths(start,end)
# print(a)