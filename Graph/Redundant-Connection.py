class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Optimal Solution: Union Find with ranking
        """
        """
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

        1) Iterate through each edge
            2) We get node1 and node2 for each edge
            3) For each node we need to find its parent -> 
                4) For each currNode, we find its parent by looking at the parent
                5) If the currNode's parent is itself, then return itself 
                6) IF the currNode's parent is not itsel , then loop until we can trace the parent 
                7) Return the parent of the current node 
            8) Once we have the parent node of currNode, we check which parent has a larger rank 
            9) The parent with the larger rank will have the smaller parent merge together
            ! If both nodes have the same parent, then that means that have been connected already prior, and this is the redundant edge 
        10) That concludes one edge, and we do so until we are done
        """

        # TODO: Instantiate the parent and rank arrays first 
        parent = [ i for i in range(len(edges) + 1)]
        rank = [ 1 for _ in range(len(edges) + 1)]
        print(f"parent: {parent}")
        print(f"rank: {rank}")
        
        # TODO: find() to find the current node's parent
        def find(currNode) -> int: 
            # * Find the currNode's parent by first degree to determine if node is a parent of itself
            candidate_par = parent[currNode]
            print(f"candidate_par: {candidate_par} for currNode: {currNode}")
            # ? The daddy node will be it's own parent; or this is a node that has not been touched yet, which is also ok 
            while (candidate_par != currNode):
                # ? Loop until we can find the current node's parent, 
                candidate_par = parent[candidate_par]
                currNode = candidate_par
                print(f"candidate_par in the while loop: {candidate_par}; currNode: {currNode}")
            print(f"Final verdict of candidate_par: {candidate_par} for currNode: {currNode}")
            return candidate_par

        # TODO: union function implementation 
        def union(node1, node2) -> bool:
            # Check for the node's parents first 
            par1 = find(node1)
            par2 = find(node2)
            print(f"par1: {par1}, par2: {par2}")

            # * If the nodes share the same parent, then it means that the current edge is redundant 
            if (par1 == par2): 
                return False 
            
            #! IF we reached here, then we either have to merge the larger / node1 (if both node's rank are the same)
            # * If node1 has a higher or equal rank, then we attach node2 as a child to node1 
            if (rank[node1] >= rank[node2]): 
                print(f"{node1} has a higher or equal rank, so we attach {node2} as a child to {node1}")
                parent[node2] = node1
                rank[node1] += rank[node2]
                print(f"rank[node1] after merge: {rank[node1]}")
            else: 
                print(f"{node2} has a higher rank, so we attach {node1} as a child to {node2}")
                parent[node1] = node2
                rank[node2] += rank[node1]
                print(f"rank[node2] after merge: {rank[node2]}")
            # ? Return True so that we can keep looping until we find the problematic edge. 
            return True 


        # TODO: Main loop to process each edge, by extracting both nodes per iteration 
        for node1, node2 in edges:
            # * If the union returns false, then we return the node1, node2 pairs 
            print("============== New Layer ===============")
            print(f"About to investigate edge: {node1}, {node2}")
            if not union(node1, node2): 
                print(f"Found redundant edge: {node1}, {node2}")
                return [node1, node2]
        








        """  ! Not optimal solution
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

        """