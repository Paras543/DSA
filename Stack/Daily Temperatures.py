class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while len(st) > 0  and temperatures[st[-1]] <= temperatures[i]:
                st.pop()

            if len(st) == 0:
                ans[i] = 0

            else:
                ans[i] = st[-1] - i 


            st.append(i)
            



        return ans


