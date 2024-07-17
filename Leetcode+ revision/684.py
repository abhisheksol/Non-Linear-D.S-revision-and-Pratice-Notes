from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent and rank arrays
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            # Path compression
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            # Find the root of each node
            p1, p2 = find(n1), find(n2)
            
            # If they share the same root, the edge is redundant
            if p1 == p2:
                return False
            
            # Union by rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        # Process each edge
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

# Example usage
edges = [[1, 2], [1, 3], [2, 3]]
solution = Solution()
print(solution.findRedundantConnection(edges))  # Output: [2, 3]
