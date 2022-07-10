def lenLongestFibSubseq(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i
    ans = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a, b = arr[i], arr[j]
            k = 2
            while a + b in d:
                a, b = b, a + b
                k += 1
                ans = max(ans, k)
    return ans

print(lenLongestFibSubseq([1,3,5]))
    


