class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == "0" or num2 == "0":
            return "0"


        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                multiply = int(num1[i]) * int(num2[j])
                pos2 = i+j+1
                pos1 = i+j


                total = ans[pos2] + multiply
                ans[pos2] = total % 10
                ans[pos1] += total // 10


        result = "".join(map(str, ans)).lstrip("0")

        return result
               

               


                


        
      