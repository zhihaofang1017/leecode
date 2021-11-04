def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    n_list = []
    result_list = []
    for i in range(1, n + 1):
        n_list.append(i)
    for t in range(n, 0, -1):
        position = (k // abc(n - 1))
        rest = (k % abc(n - 1))
        if rest != 0:
            result_list.append(n_list[position])
            n_list.remove(n_list[position])
            n = n - 1
            k = rest
        else:
            position = position - 1
            result_list.append(n_list[position])
            n_list.remove(n_list[position])
            result_list = result_list + n_list[::-1]
            break
    result_list = [str(x) for x in result_list]
    result = "".join(result_list)
    print(result)

def abc(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


getPermutation(3, 3)
