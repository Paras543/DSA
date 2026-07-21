class Solution(object):


    def check_frequencing(self,word):
        freq = [0] * 26 
        for ch in word:
            index = ord(ch) - ord('a')
            freq[index] += 1 
        return tuple(freq)



    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}
        for word in strs:
            key = self.check_frequencing(word)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
        

        
