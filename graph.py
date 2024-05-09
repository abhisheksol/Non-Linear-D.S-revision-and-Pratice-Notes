class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}
        for i, j in self.edges:
            if i in self.dict:
                self.dict[i].append(j)
            else:
                self.dict[i] = [j]
        print(self.dict)

    def find_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.dict:
            return []

        all_path = []
        for node in self.dict[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                print(new_path)
                for p in new_path:
                    all_path.append(p)
        print(all_path)


obj = [
    ("mumbai", "pune"),
    ("mumbai", "kholapur"),
    ("pune", "solapur"),
    ("kholapur", "solapur")
]
i = Graph(obj)
i.find_path("mumbai", "solapur")
