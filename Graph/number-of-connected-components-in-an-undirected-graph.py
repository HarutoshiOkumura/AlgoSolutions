"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
"""
# ! Do we need to be able to handle loops? I will assume no first
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        next = {}
        visited = set()
        count = 0
        # TODO: Initialize the adjacency with the nodes first 
        for node in range(n):
            next[node] = []
        print(f"Initial next: {next}")
        
        # TODO: Populate the next node in regards to the current node
        for node1, node2 in edges: 
            next[node1].append(node2)
            next[node2].append(node1)
        print(f"After populating next: {next}")
        
        # * Make sure to consider logic for loop if it fails hidden test cases 
        def DFS(currNode, prevNode): 
            """
            Base case needed if we need loop detection
            """
            print(f"================ New Layer ================")

            visited.add(currNode)
            print(f"Visited: {visited}")
            
            # TODO: I am going to assume that each node can have multiple edges connected it
            for nextNode in next[currNode]:
                print(f"Next node: {nextNode}, given currNode: {currNode}")
                if (nextNode != prevNode and nextNode not in visited):
                    print(f"Next node: {nextNode}, given currNode: {currNode} is not in visited; calling DFS({nextNode})")
                    DFS(nextNode, currNode)
            return 

        # TODO: For-loop through all the nodes, check to make sure if it even needs the DFS 
        for currNode in range(n):
            if not (currNode in visited):
                print(f"currNode: {currNode} is not in visited; calling DFS({currNode})")
                DFS(currNode, -1)
                count += 1
                print(f"count: {count}")
        return count

