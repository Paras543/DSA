#3 solve it one more time
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q1 = deque()
        result = []

        for i in range(k):
            while len(q1) > 0 and nums[q1[-1]] <= nums[i]:
                q1.pop()

            q1.append(i)

        for i in range(k,len(nums)):
            result.append(nums[q1[0]])

            while len(q1) > 0 and q1[0] <= i-k:
                q1.popleft()

            while len(q1) > 0 and nums[q1[-1]] <= nums[i]:
                q1.pop()

            q1.append(i)

        result.append(nums[q1[0]])

        return result

    





        