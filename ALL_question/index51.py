import copy


def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    list_result = []
    list_n = ["y"] * n * n
    for i in range(0, n):
        list_result.append(list_n[n * i:n * (i + 1)])
    solution2(0, n, list_result)


def solution2(a, n, list_result):
    list_result_all = []
    for i in range(a, n):
        list_result_all.append(copy.deepcopy(list_result))
        for j in range(0, n):
            if list_result[i][j] == 'y':
                a = solution(i, j, list_result)
                if not a:
                    list_result[i][j] = '.'
                else:
                    list_result = a
        if list_result[i] == ["."] * n:
            solution2(i-1, n, list_result_all[i])

    print(list_result_all)


def solution(i, j, list_result):
    list_result_none = copy.deepcopy(list_result)
    for k in range(0, len(list_result)):
        list_result[i][k] = '.'
        list_result[k][j] = '.'
        if len(list_result) > i + k >= 0 and len(list_result) > j + k >= 0:
            list_result[i + k][j + k] = '.'
        if len(list_result) > i + k >= 0 and len(list_result) > j - k >= 0:
            list_result[i + k][j - k] = '.'
    if i != len(list_result) - 1 and list_result[i + 1] == ['.'] * len(list_result):
        return False
    else:
        list_result[i][j] = 'Q'
        return list_result


solveNQueens(4)
