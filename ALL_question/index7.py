
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    list_s = list(str(x))
    list_s = list_s[::-1]
    result = 0
    if list_s[-1] == "-":
        list_s = list_s[0:-1]
        for i in range(0, len(list_s)):
            result = result + int(list_s[len(list_s) - i - 1]) * (10 ** i)
        result = -result
    else:
        for i in range(0, len(list_s)):
            result = result + int(list_s[len(list_s) - i - 1]) * (10 ** i)
    if result > 2**31-1 or result < -2**31:
        return 0
    return result

print(reverse(12300))