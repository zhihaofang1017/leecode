def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    all_data = []
    result = []
    result_cor = []
    i = 0
    j = 0
    for k in range(0, len(matrix)):
        all_data = all_data + matrix[k]
    result.append(matrix[i][j])
    result_cor.append([i, j])
    while len(result) != len(all_data):
        while j + 1 < len(matrix[0]) and [i, j + 1] not in result_cor:
            result.append(matrix[i][j + 1])
            result_cor.append([i, j + 1])
            j = j + 1
        while i + 1 < len(matrix) and [i + 1, j] not in result_cor:
            result.append(matrix[i + 1][j])
            result_cor.append([i + 1, j])
            i = i + 1
        while j - 1 >= 0 and [i, j - 1] not in result_cor:
            result.append(matrix[i][j - 1])
            result_cor.append([i, j - 1])
            j = j - 1
        while i - 1 >= 0 and [i - 1, j] not in result_cor:
            result.append(matrix[i - 1][j])
            result_cor.append([i - 1, j])
            i = i - 1
    print(result)


spiralOrder([[23, 18, 20, 26, 25], [24, 22, 3, 4, 4], [15, 22, 2, 24, 29], [18, 15, 23, 28, 28]])
