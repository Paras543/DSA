class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        a = False
        b = False
        c = False

        for x,y,z in triplets:
            if x<=target[0] and y<= target[1] and z <= target[2]:
                if x == target[0]:
                    a =  True
                if y == target[1]:
                    b =  True
                if z == target[2]:
                    c =  True

        return a and b and c
        