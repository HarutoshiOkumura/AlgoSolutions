from typing import List

"""
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        # TODO: Create the hash empty mapping first, so that nodes not covered in edges will not be missed 
        adj = { i:[] for i in range(n) }

        # TODO: Build the adjacency list first
        for node1, node2 in edges: 
            # Mark Node 1 as neighbour of node 2 
            adj[node1].append(node2)
            # Mark Node 2 as neighbour of node 1 
            adj[node2].append(node1)

        if n <= 1: return True
        
        # TODO: Implement the DFS traversal to starts at 0 -> I think we only do one pass, to also ensure that everything is connected by being traversable in ONE PASS 
            # * 1) prev: keep track of the previous node to avoid repeat 
        def DFS(currNode, prevNode): 
            """
            Base Cases
            """
            # If the current node has already been visited, then it means that there is a loop detected 
            if (currNode in visited): 
                return False

            """
            Main Traversal Logic - Explore deeper DFS depth
            """
            # At here, the node have not been visited yet, so we add it to the logic 
            visited.add(currNode)

            # ? Now that we have visited current Node, next we need to check its neighbor
            for neighbor in adj[currNode]: 
                # ! We have to ensure that the visited not is not prevNode
                if (neighbor == prevNode): 
                    continue
                
                if not (DFS(neighbor, currNode)):
                    return False
            return True
        DFS(0, -1) and n == len(visited)

