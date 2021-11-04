def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    total = 1
    for i in range(1,n//2 + 1):
        count = n - i
        temp = 1
        for j in range(i):
            temp = temp * (count - j) // (j+1)
        total = total + temp
    print(total)


climbStairs()