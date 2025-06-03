from typing import List


"""
Implementation Steps: 
    1) DFS to go through all the noes that represent a course 
    2) Stopping condition is when numCourses == len(visitedSet())
    3) Build the dependency hashmap: 
        a) Dependency{} --> course : [Course they are dependent on]
        b) When DFS traversing, we will be using this hashmap 
        c) When we traverse to a new course, we check if it has any dependencies or not, if not then this course can be taken 
    4) Maintain a visitedSet() to keep track of all the courses that have been processed already 

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyHash = {}
        visitedSet = set()
        # TODO: Iteratively populate the dependency mapping 
        for dependency in prerequisites: 
            # [0] depends on [1] --> [[0,1]]
            # * If its the first instance of dependency[0], then it creates a new key, then appends the dependency to the 
            dependencyHash.setdefault(dependency[0], []).append(dependency[1])