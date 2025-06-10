class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TODO: Instantiate and populate the dependency hashmap 
        adj = {}
        for course in range(numCourses):
            adj[course] = []
        
        print(f"This is what adj before populating: {adj}")
        
        # TODO: Need to populate the dependency hashmap 
        for course, prereq in prerequisites: 
            adj[course].append(prereq)
        
        print(f"This is what adj after populating: {adj}")
        
        visited = [] # Trying List instead to gauge out methods to preserving insertion order
        visiting = set()
        # For each course given, we find if all of its prerequisites can be satisfiable, if yes then this course itself can be satisfied 
        def dfs(course):
            """
            Base case determinations 
            """
            # ! Base Case 1
            # TODO: If the current course has already been visited (verified to have no loops above and can be completed), then just return 
            if (course in visited): 
                print(f"Course: {course} has already been visited")
                return True
            
            # ! Base Case 2 
            # TODO: If the current course is still in the current recursive path, and we find out that it is in the visiting(), then there is a loop
            if (course in visiting):    
                print(f"Course: {course} is in the visiting set")
                return False
            
            # TODO: Add the current course into visiting, so that we can check if this course is in the loop (have been visited alr in the current recursive path)
            visiting.add(course)
            print(f"Course: {course} has been added to the visiting set")

            # * At this point, we have verified that the current course is: 
                # 1) Not confirmed to be safe / completable 
                # 2) The course is not the head of the loop 
            # TODO: We still need to verify if the current course has any prerequisites, and if it does, are the prerequisites in the visited? 
            for prereq in adj[course]: # Either be 1) empty, 2) one element 3) an array of prerequisites
                # ? A) We need to validate each prereq can be finished, if they can be finished, then it will trigger Base Case 1 
                # ? B) If the course cannot be finished, then it will be triggered by Base Case 2
                # ? C) If its neither, then we have to DFS deeper until we can answer Option A or Option B 
                # TODO: If it returns True, then it can be finished, if it returns false, then it cannot be finished 
                print(f"About to check prereq: {prereq} in DFS")
                if  not (dfs(prereq)): 
                    print(f"Prereq: {prereq} is not valid")
                    return False 
                
            # * If we can clear the entire prereq list (for the current course), then we can safely add the current course to visited
            # TODO: Add the course into visiting as we know it is valid; remove it from visiting as we have finished checking the current course's prerequisites recursivel 
            visiting.remove(course)
            visited.append(course)
            print(f"Course: {course} has been added to the visited list")
            return True
        # =============================== End of the DFS ===============================

        # TODO: Iterate through every course to account for isolated courses as well 
        for course in range(numCourses): 
            # ! If the current course does have a loop, then the DFs will return False, to which we respond wih False for the findOrder()
            print(f"About to check course: {course} in DFS")
            if not (dfs(course)): 
                return []
            print(f"Course: {course} is valid")
        
        # ? Due to the fact that we only count a course to be visited if we can make sure that all of its descendants are valid (Can be finished 
        # ! This means that courses with the least amount of in-degree will be the first to be appended, resulting in a topological sort
        return visited

