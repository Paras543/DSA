class Solution(object):
    def ispalindromic(self,s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def getallpart(self,s,partition,ans):
        if len(s) == 0:
            ans.append(partition[:])
            return 

        for i in range(len(s)):
            part = s[0:i+1]
            if self.ispalindromic(part):
                partition.append(part)

                self.getallpart(s[i+1:],partition,ans)
                partition.pop()



    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partition = []
        ans = []
        self.getallpart(s,partition,ans)

        return ans



        