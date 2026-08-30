import heapq
from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = Counter(s)
        max_heap = [(-count,char) for char,count in freq.items()]
        heapq.heapify(max_heap)

        result = []
        prev_count = 0
        prev_char = " "

        while max_heap:
            count,char = heapq.heappop(max_heap)
            result.append(char)
            count += 1

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

           
            prev_count = count
            prev_char = char

        if prev_count < 0:
            return ""

        return "".join(result)









       
        