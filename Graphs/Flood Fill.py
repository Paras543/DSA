class Solution(object):
    def dfs(self,image,i,j,newcolor,original_color):
        if i<0 or j <0 or i>= len(image) or j >= len(image[0]) or image[i][j] is not original_color or image[i][j] == newcolor:
            return 
        image[i][j] = newcolor
        self.dfs(image,i-1,j,newcolor,original_color)
        self.dfs(image,i,j+1,newcolor,original_color)
        self.dfs(image,i+1,j,newcolor,original_color)
        self.dfs(image,i,j-1,newcolor,original_color)

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.dfs(image,sr,sc,color,image[sr][sc])
        return image