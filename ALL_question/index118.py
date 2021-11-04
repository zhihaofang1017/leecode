def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    temp = [[1]]
    for i in range(1,numRows):
        temp1 = []
        for j in range(i+1):
            if j == 0:
                temp1.append(1)
            elif j == i:
                temp1.append(1)
            else:
                a = temp[i - 1][j] + temp[i - 1][j - 1]
                temp1.append(a)
        temp.append(temp1)
        print(temp)

generate(6)