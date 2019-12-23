class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)

        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix


a = Solution()

matrix = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
a.rotate(matrix)
