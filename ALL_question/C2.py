def Permutation():
    test_num = int(input())
    for i in range(test_num):
        num_count = int(input())
        List1 = input()
        List1 = List1.split(" ")
        List1 = list(map(int,List1))
        if List1 == sorted(List1):
            print(0)
            continue
        if List1[0] == 1 or List1[-1] == num_count:
            print(1)
        elif List1[0] == num_count and List1[-1] == 1:
            print(3)
        else:
            print(2)
Permutation()