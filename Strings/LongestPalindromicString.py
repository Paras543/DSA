class Solution(object):

    


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s 

        start = 0
        max_len = 1

        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1

            return left + 1 , right - 1





        for i in range(len(s)):
            left,right = expand(i,i)
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1

            left,right = expand(i,i+1)
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1



        return s[start:start + max_len]

            


            



           

                 



            




                

        