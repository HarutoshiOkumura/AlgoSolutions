class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        adj = {}
        # TODO: Loop through edges array to get the pairs of nodes 
        for node1, node2 in edges: 
            # * Document how both nodes point at each other (undirected)
            adj.setdefault(node1, []).append(node2)
            adj.setdefault(node2, []).append(node1)

        # TODO: DFS 
        def DFS(currNode , prevNode):
            print("============== New Layer ===============")
            print(f"currNode: {currNode}, prevNode: {prevNode}")
            print(f"visited: {visited}")
            print(f"adj: {adj}")

            # We we find the node in visite , then there is a loop 
            if (currNode in visited):
                print(f"currNode: {currNode} is in visited; returning [currNode, prevNode]")
                return [currNode, prevNode]
            
            # ? If it doesn't pass the case then we can safely add th currNoe to  visited
            visited.add(currNode)
            print(f"currNode: {currNode} is added to visited")

            #* Now traverse through all of its neighbors
            for neighbor in adj[currNode]:
                if not (neighbor is prevNode):
                    print(f"neighbor: {neighbor} is not prevNode; calling DFS({neighbor}, {currNode})")
                    return DFS(neighbor, currNode)
            
            return 


        # TODO: DFS recurse on "1" to find the loop; as its' guaranteed to have a loop 
        return DFS(1, -1)
