class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        mp = {}
        st = []

        for i in range(len(nums2)-1,-1,-1):
            while len(st) > 0 and st[-1] <= nums2[i]:
                st.pop()

            if len(st) == 0:
                mp[nums2[i]] = -1

            else:
                mp[nums2[i]] = st[-1]

            st.append(nums2[i])

        ans = []
        for i in range(len(nums1)):
            ans.append(mp[nums1[i]])

        return ans

        