def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    result = 0
    while x1 != len(matrix[0]) - 1 and y1 != len(matrix) - 1:
        if matrix[x1][y1] == "1":
            for i in range(x2, len(matrix[0])):
                for j in range(y2,len(matrix)):
                    a = solution(x1, y1, i, j, result)
        else:
            if x1 == len(matrix[0] - 1):
                x1 = 0
                y1 = y1 + 1
            elif x1 == len(matrix[0]) - 1 and y1 == len(matrix) - 1:
                print("1")
            else:
                x1 = x1 + 1

def solution(x1, y1, x2, y2, result):
    if (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) <= result:
        return result

    x1 = x1 + 1
    y1 = y1 + 1
    x2 = x2 + 1
    y2 = y2 + 1
    return x1,y1,x2,y2

maximalRectangle([])