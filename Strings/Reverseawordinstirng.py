class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ans = ""
        i = 0

        while i < len(s):
            word = ""

            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1
                
            ans += word[::-1]

            while i < len(s) and s[i] == " ":
                ans += s[i]
                i += 1

            
        return ans
    
    