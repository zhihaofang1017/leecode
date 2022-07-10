def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    n = len(s)
    ans = [0] * n

    idx = -n
    for i, ch in enumerate(s):
        if ch == c:
            idx = i
        ans[i] = i - idx
        print(ans)

    idx = 2 * n
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            idx = i
        ans[i] = min(ans[i], idx - i)
        print(ans)
    return ans

shortestToChar("loveleetcode","e")