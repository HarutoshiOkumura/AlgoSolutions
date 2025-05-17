from typing import List
import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculates the minimum number of intervals required to complete all tasks
        with a cooldown period 'n' between identical tasks.

        The algorithm uses a greedy approach:
        1. Count task frequencies.
        2. Use a max-heap to prioritize tasks with the highest remaining counts.
        3. Use a cooldown queue to manage tasks that have been recently executed.
        4. Simulate time, processing one task or idling in each time unit.
        """
        
        task_counts = Counter(tasks)
        # maxHeap stores negative counts to simulate a max-heap with Python's min-heap (heapq).
        # We only need the counts, not the task characters themselves, for the greedy choice.
        maxHeap = [-count for count in task_counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        # cooldown queue stores tuples of (ready_time, task_count).
        # - ready_time: The earliest time the task can be processed again.
        # - task_count: The remaining count of that task type (stored as a negative number).
        cooldown = deque()

        # Main loop: continues as long as there are tasks to process or tasks in cooldown.
        while maxHeap or cooldown:
            # Advance time by one unit for the current cycle (either task execution or idle).
            time += 1

            # Step 1: Check and release tasks from cooldown.
            # If a task in the cooldown queue is ready (its ready_time <= current time),
            # move it back to the maxHeap to be available for scheduling.
            # Multiple tasks might become ready at the same time, hence the 'while' loop.
            while cooldown and cooldown[0][0] <= time:
                # Pop the ready task from cooldown. We are interested in its count.
                _ready_time, count_from_cooldown = cooldown.popleft()
                heapq.heappush(maxHeap, count_from_cooldown) # Add its count back to the maxHeap.

            # Step 2: Try to execute a task.
            if maxHeap:
                # Select the task with the highest frequency (most remaining instances).
                # This is the smallest (most negative) number from our min-heap.
                current_task_count = heapq.heappop(maxHeap)
                
                # "Execute" one instance of this task.
                current_task_count += 1 # Increment its count (e.g., -3 becomes -2).
                
                # If there are still instances of this task type remaining (count < 0),
                # add it to the cooldown queue.
                if current_task_count < 0:
                    # It will be ready again after 'n' intervals.
                    # If executed at 'time', next available slot is 'time + n + 1'.
                    next_available_time = time + n + 1 
                    cooldown.append((next_available_time, current_task_count))
            # else (maxHeap is empty):
                # No task is available from the heap to execute in this time slot.
                # This means the CPU is idle for this time unit.
                # 'time' has already been incremented. The loop continues, and we wait
                # for tasks to become ready from the cooldown queue in future iterations.
                # No explicit action needed for idling here; the time increment covers it.
        
        # All tasks are processed, and the cooldown queue is empty.
        return time
