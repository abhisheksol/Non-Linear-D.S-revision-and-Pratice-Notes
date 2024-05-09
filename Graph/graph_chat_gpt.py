class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.dict = {}
        for start, end in edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
        print(self.dict)

    def getpath(self, start, end, path=None):
        # If path is not provided, initialize it to an empty list
        if path is None:
            path = []

        # Add the current node to the path
        path = path + [start]

        # If we reach the end node, return the current path as a list
        if start == end:
            return [path]

        # If the current node is not in the graph, return an empty list
        if start not in self.dict:
            return []

        # Store all_paths to collect paths from recursive calls
        all_paths = []

        # Explore neighbors of the current node
        for node in self.dict[start]:
            # Ensure the neighbor is not already in the path to avoid cycles
            if node not in path:
                # Recursively find paths from the neighbor to the end
                new_paths = self.getpath(node, end, path.copy())
                print("new_path",new_paths)
                # Extend the list of all_paths with the new_paths
                all_paths.extend(new_paths)

        # Return the list of all_paths
        return all_paths


a = [
    ("mumbai", "pune"),
    ("mumbai", "kholapur"),
    ("pune", "solapur"),
    ("kholapur", "solapur"),
]

start = "mumbai"
end = "solapur"
i = Graph(a)
print("====")
print(i.getpath(start, end))
