import heapq
from typing import List, Tuple
"""
Learning Outcomes: 
1. Heap key first: By putting dist as the first element in the tuple (or by using the key=… argument), the heap knows to order by distance.
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # In the array points[i], there is the i-th point with its x and y coordinates 
        # Return the k closest points to the origin (0,0)
        # Use euclidean distance 
        """
        1. Compute all the Euclidean, don't even have to Sqrt it 
        2. Add the computed metrics to the rd spot (index 2) in the original arrays
        3. When heapifying, point towards the (2nd index) for computing the min-heap
        4. We use min-heap as we want the shortestest distances
        5. And then heapq.heappop k times 
        6. Slice to only return only the first 2 numbers in each array 
        """
        # 1. Build a heap of (distance, x, y)
        heap: List[Tuple[int,int,int]] = []
        for x, y in points:
            dist_sq = x*x + y*y
            heap.append((dist_sq, x, y))
        
        # 2. Heapify once (O(n))
        heapq.heapify(heap)
        
        # 3. Extract the k smallest by distance
        answer: List[List[int]] = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            answer.append([x, y])
        
        return answer


