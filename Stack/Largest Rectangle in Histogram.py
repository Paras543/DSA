class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        st = []
        right =  [0] * len(heights)
        left = [0] * len(heights)

        for i in range(len(heights)-1,-1,-1):
            while len(st) > 0 and heights[st[-1]] > heights[i]:
                st.pop()
            if len(st) == 0:
                right[i] =  len(heights)
            else:
                right[i] = st[-1]
            st.append(i)

        for i in range(len(heights)):
            while len(st) > 0 and heights[st[-1]] > heights[i]:
                st.pop()
            if len(st) == 0:
                left[i] =  len(heights)
            else:
                left[i] = st[-1]
            st.append(i)


        ans = 0
        for i in range(len(heights)):
            width = right[i] - left[i] - 1
            current_area = heights[i] * width
            ans = max(current_area,ans)

        return ans

    



            