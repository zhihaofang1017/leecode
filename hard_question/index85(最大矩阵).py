def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    List = []
    for i in range(len(matrix)):
        temp = []
        count = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == "1":
                count = count + 1
                temp.append(count)
            else:
                count = 0
                temp.append(count)
        List.append(temp)
    print(List)
    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            height = 0
            for k in range(i, len(matrix)):
                if List[i][j] <= List[k][j] and List[i][j] != 0:
                    height = height + 1
                else:
                    break
            for k in range(i-1, -1, -1):
                if List[i][j] <= List[k][j]and List[i][j] != 0:
                    height = height + 1
                else:
                    break
            ans = max(ans,height*List[i][j])
    return ans




maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
