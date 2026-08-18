class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        st = []
        path = path.split('/')
        

        for component in path:
            if component == "" or component == ".":
                continue
            elif component == "..":
                if st:
                    st.pop()
            else:
                st.append(component)

            


        result = "/" + "/".join(st)
        return result

                

        
        