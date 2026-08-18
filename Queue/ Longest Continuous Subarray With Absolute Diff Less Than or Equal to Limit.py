from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        q1 = deque() ## Decreasing
        q2 = deque() ## Increasing
        left = 0
        answer = 0

        for right in range(len(nums)):
            
            while q1 and  nums[right] > q1[-1]:
                q1.pop()
            q1.append(nums[right])
            while q2 and  nums[right] < q2[-1]:
                q2.pop()
            q2.append(nums[right])
           

            while q1[0] - q2[0] > limit:
                if q1[0] == nums[left]:
                    q1.popleft()
                if q2[0] == nums[left]:
                    q2.popleft()

                left += 1
                
            answer = max(answer,right-left + 1)
        return answer

                

        

            

        