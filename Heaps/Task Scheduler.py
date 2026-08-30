import heapq
from collections import Counter, deque

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        
        count = Counter(tasks)

        
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        
        q = deque()

        time = 0

        while max_heap or q:
            time += 1

            
            if q and q[0][1] == time:
                cnt, available_time = q.popleft()
                heapq.heappush(max_heap, cnt)

            
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1

                
                if cnt < 0:
                    q.append([cnt, time + n + 1])

        return time
    
    ## Solve again all the question of the heaps
