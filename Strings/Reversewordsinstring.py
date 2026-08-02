class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        
        s = s[::-1]

        ans = ""
        i = 0

        while i < len(s):

            
            while i < len(s) and s[i] == " ":
                i += 1

            word = ""

           
            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1

            
            if len(word) > 0:
                if len(ans) > 0:
                    ans += " "
                ans += word[::-1]

        return ans
    
    