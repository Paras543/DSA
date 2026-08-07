class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n == 1:
            return 0

        mid = 2 ** (n-2)

        if k <= mid:
            return self.kthGrammar(n-1,k)
        else:
            return 1 -  self.kthGrammar(n-1,k-mid)



## revise it once more and the mid condtion is the mid = 2 ** n-2 where we calcualte the middle part and then traverse through the mid either we go left half or the right half