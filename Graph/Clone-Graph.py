
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # We are given the starting node here 
        self.oldNewHash = {} # TODO: originalNode : newNode
        
        # ! Important to remember that all 'node" being passed in are from the original graph, not the deepcopy one 
        def dfs(node): 
            """
            Base Cases 
            """
            # Return if the node already has mapping. 
            if (node in self.oldNewHash):
                return self.oldNewHash[node]
            
            # * If it doesn't exist then add one 
            if (node not in self.oldNewHash):
                newNode = Node(node.val)
                self.oldNewHash[node] = newNode
            """
            Modifications to current Node 
            """
            for candidate in node.neighbors:
                newNode.neighbors.append(dfs(candidate))
            return newNode



            # ! Old Attempt 
            """
            # TODO: 1) Access the node's copy first (L2)
            copyNode = self.oldNewHash.get(node)
            # TODO: 2) Start constructing the adjacency list for this node 
            # 2a) if the neighbors doesn't exist 
            if (copyNode.neighbors is None):
                copyNode.neighbors = []
                copyNode.neighbors.append(copyNode)
            # 2b) if the neighbors does exist
            else:
                copyNode.neighbors.append(copyNode)
            # Loop through the graph until we get the original code again? 
            # ? Splitting into left and right sub paths 
            # TODO: Split left 
            dfs(node.neighbors[0])

            # TODO: Split right 
            dfs(node.neighbors[1])
            """


        return dfs(node) if node else None 
       

        