def Hit():
    All = input()
    All = int(All)
    length = input()
    length = int(length)
    String = input()
    String = list(String)
    lst2 = list(set(String))
    from collections import Counter
    a = Counter(String)

    print(a.index(min(a)))




Hit()