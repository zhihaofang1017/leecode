def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    result_list = []
    if numRows == 1:
        return s
    for i in range(0, numRows):
        result_list.append([])
    s_list = list(s)
    line = 0
    judege = 0
    for i in range(0, len(s_list)):
        result_list[line].append(s_list[i])
        if judege == 0:
            if line == numRows-1:
                judege = 1
                line = line - 1
            else:
                line = line + 1
        else:
            if line == 0:
                judege = 0
                line = line + 1
            else:
                line = line - 1
    result = []
    for i in range(0, numRows):
        result = result + result_list[i]
    result = ''.join(result)
    print(result)

convert('ABC',2)