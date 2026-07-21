class Solution(object):
    def character_hashing1(self,s):
        freq1 = {}

        for ch in s:
                freq1[ch] = freq1.get(ch,0) + 1
        return freq1

    def character_hashing2(self,t):
        freq2 = {}

        for ch in t: 
                freq2[ch] = freq2.get(ch,0) +1 
        return freq2




    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        


        freq1 = self.character_hashing1(s)
        freq2 = self.character_hashing2(t)

        if freq1 == freq2:
            return True
        else:
            return False

            
     


        


        
