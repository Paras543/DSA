class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        st = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in '({[':
                st.append(ch)

            else:
                if len(st) == 0:
                    return False
                if st[-1] != pairs[ch]:
                    return False

                st.pop()

        return len(st) == 0

      
       



