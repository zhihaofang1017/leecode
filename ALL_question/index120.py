def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    temp = [triangle[0]]
    for i in range(1,len(triangle)):
        temp1 = []
        for j in range(len(triangle[i])):
            if j == 0:
                temp1.append(temp[i-1][0] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                temp1.append(temp[i - 1][-1] + triangle[i][j])
            else:
                a = min(temp[i - 1][j] + triangle[i][j],temp[i - 1][j - 1] + triangle[i][j])
                temp1.append(a)
        temp.append(temp1)
    print(temp)
    print(min(temp[-1]))
minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])