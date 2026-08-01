class Solution(object):
    def isalphanumeric(self,ch):
            if( ch >= '0' and ch <= '9') or (ch.lower() >= 'a' and ch.lower() <= 'z'):
                return True
            return False


    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        st = 0 
        end = len(s) - 1
        while(st<end):
            if not self.isalphanumeric(s[st]):
                st += 1
            if not self.isalphanumeric(s[end]):
                end -= 1
            if (s[st].lower() != s[end].lower()):
                return False
            st += 1
            end -= 1
        return True

