class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
      
        st = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                st.append(int(token))
            else:
                b = st.pop()
                a = st.pop()

                if token == '+':
                    st.append(a + b)
                if token == '*':
                    st.append(a * b)
                if token == '-':
                    st.append(a - b)

                if token == '/':
                    result = abs(a) // abs(b)

                    if (a < 0) != (b < 0):
                        result = -result

                    st.append(result)

        return st[-1]



        
