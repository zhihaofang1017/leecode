def Delete():
    test_num = int(input())
    for i in range(test_num):
        num_count = int(input())
        List1 = input()
        List1 = List1.split(" ")
        List1 = list(map(int,List1))
        avg = sum(List1)/num_count
        print(avg)

Delete()