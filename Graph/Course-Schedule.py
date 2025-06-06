from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1) Build a full adjacency list so that every course 0..numCourses-1 appears as a key.
        adj = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # 2) We’ll use two sets to detect cycles:
        #    - visiting:   courses currently on the recursion stack
        #    - visited:    courses already fully processed (no cycle from them)
        visiting = set()
        visited = set()

        def dfs(node: int) -> bool:
            # TODO: 2) Base cases for checking if the nodes is valid or not 
                # * 1) If the node is in the visiting set, then we have already visited it in this recursive call stack, so we have a cycle 
                # * 2) If the node is in the visited set, then we have already checked it before and found no cycles.
            # If we see 'node' is already in visiting, there's a back-edge → cycle.
            if node in visiting:
                return False
            # If 'node' is already in visited, we've checked it before and found no cycles.
            if node in visited:
                return True

            # Mark this node as “currently visiting”
            visiting.add(node)

            # Recurse on all prerequisites of 'node'
            for prereq in adj[node]:
                if not dfs(prereq):
                    return False

            # TODO:  3) We are done with all of the children, which are the prerequisites of the current node, this means that the current node is validated 
            # TODO:  so the course can be completed, so FROM NOW ON, when we encounter this node, it means that we have already checked it before and found no cycles.
            # Done exploring all children: move node from visiting → visited
            visiting.remove(node)
            visited.add(node)
            return True

        # TODO: 1) Iteratively calling the DFS traversal 
        # 3) Call DFS on every course that hasn’t been visited yet.
        for course_id in range(numCourses):
            if course_id not in visited:
                if not dfs(course_id):
                    return False

        # If no cycle was detected in any DFS, we can finish all courses.
        return True


if __name__ == "__main__":
    # Example test case from the explanation:
    numCourses = 6
    prerequisites = [
        [1, 0],  # to take course 1 you must first take course 0
        [2, 0],  # to take course 2 you must first take course 0
        [3, 1],  # to take course 3 you must first take course 1
        [3, 2],  # to take course 3 you must first take course 2
        [4, 3],  # to take course 4 you must first take course 3
        [5, 4]   # to take course 5 you must first take course 4
    ]

    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(f"Can finish all courses? {result}")  # Expected output: True
