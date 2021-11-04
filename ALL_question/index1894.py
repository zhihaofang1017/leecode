def chalkReplacer(chalk, k):
    """
    :type chalk: List[int]
    :type k: int
    :rtype: int
    """
    length = sum(chalk)

    a = k - length * (k // length)

    temp = 0
    j = 0
    print(a)
    while temp <= a:
        temp = temp + chalk[j]
        j = j + 1
    print(j - 1)

chalkReplacer([5,1,5],27)