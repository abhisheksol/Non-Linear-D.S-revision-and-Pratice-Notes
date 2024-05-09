class Graph:
    def __init__(self,edges) -> None:
        self.edges=edges
        self.dict={}
        for start, end in edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start]=[end]
        # print(self.dict)

    def getpath(self,start,end,path=[]):
       
        path=path+[start]

        if start==end:
            return [path]
        
        if start not in self.dict:
            return
        
        all_path=[]
        for node in self.dict[start]:
            if node not in path:
                new_path=self.getpath(node,end,path)
                # print(new_path)
                for p in new_path:
                    all_path.append(p)
        return all_path
        

a=[
    ("mumbai","pune"),
    ("mumbai","kholapur"),
    ("pune","solapur"),
    ("kholapur","solapur")
     
   ]
start="mumbai"
end="solapur"
i=Graph(a)
print("====")
print(i.getpath(start,end))


