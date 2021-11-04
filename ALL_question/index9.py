def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if list(str(x)) == list(str(x))[::-1]:
        return True
    else:
        return False

print(isPalindrome(-1221))