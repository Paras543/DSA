

class Solution(object):
    def isfreqsame(self,freq1,freq2):
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True
 
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        freq = [0] * 26 
        window_freq = [0] * 26 

        for ch in s1:
            freq[ord(ch) - ord('a')] += 1

        window_size =  len(s1)
        for i in range(window_size):
            window_freq[ord(s2[i])-ord('a')] += 1

        
        if self.isfreqsame(freq,window_freq):
            return True 

        left = 0

        for right in range(window_size,len(s2)):

            window_freq[ord(s2[left]) - ord('a')] -= 1

            window_freq[ord(s2[right])-ord('a')] += 1

            left += 1

            if self.isfreqsame(freq,window_freq):
                return True

        return False




            

            
        
        