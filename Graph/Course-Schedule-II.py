class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [] # Trying List instead to gauge out methods to preserving insertion order
        visiting = {}
        # For each course given, we find if all of its prerequisites can be satisfiable, if yes then this course itself can be satisfied 
        def dfs(course):
            # Base cases to determine if there are any 