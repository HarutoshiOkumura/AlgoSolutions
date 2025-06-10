# from typing import List

"""
Kahn's Algorithm Implemented 

1) Repeatedly trying to find vertices that have an in-degree == 0 (i.e. no imcoming edge)
2) If the vertices A have in-degree of zero, then we remove it from the graph 
3) To all the vertices that have an in-degree from vertex A, we decrement those vertices' in-degree
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        indegreeMap = {}
        dependencyHash = {}
        topologicalSort = []

        # TODO: Initialize each course's in-degree tracker first 
        for course in range(numCourses):
            # Initialized to 0 in-degree first 
            indegreeMap[course] = 0 
            dependencyHash[course] = []
        print(f"Initialized the indegreeMap and dependencyHash: \n {indegreeMap} and \n {dependencyHash}")
        
        # TODO: Populate the in-degree mapping 
        for course, prereq in prerequisites: 
            indegreeMap[course] += 1 
            dependencyHash[prereq].append(course)
            print(f"Populated the indegreeMap and dependencyHash: \n {indegreeMap} and \n {dependencyHash}")
            
        #! Now we have all course's indegree metric accessible in O(1) time complexity 

        #* Initially append all the indegree with 0, also check if we can even BFS or not 
        initialState = False 
        for course in range(numCourses): 
            if (indegreeMap[course] == 0):
                queue.append(course)
                print(f"Appended the course: {course} to the initial queue")
                initialState = True
        # If we cannot find any courses with in-degree of 0, then there is definately a loop 
        if not initialState: 
            print(f"No courses with in-degree of 0 found, returning empty list")
            return []
        
        # TODO: Now we BFS our way through the entire dependency graph until its empty 
        print(f"Starting to BFS =================================")
        while queue: 
            course = queue.popleft()
            topologicalSort.append(course)
            print(f"Appended the course: {course} to the topologicalSort")

            for dependent_course in dependencyHash[course]: 
                indegreeMap[dependent_course] -= 1
                
                if indegreeMap[dependent_course] == 0:
                    queue.append(dependent_course)
        
        if (len(topologicalSort) != numCourses):
            return []
        return topologicalSort
            