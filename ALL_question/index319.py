def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    hashtable = dict()
    for i in range(n):
        hashtable[i] = 0

    for i in range(n):
        hashtable[i] = 0

    print(hashtable[1])
    hashtable[1]= hashtable[1] + 1
    print(hashtable[1])

bulbSwitch(10)

