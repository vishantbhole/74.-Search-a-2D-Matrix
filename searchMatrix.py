
#74. Search a 2D Matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        res = []
        if not matrix:
            return res


        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
