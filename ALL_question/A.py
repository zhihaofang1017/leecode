def Partition():
    num = input()
    num = int(num)
    List = input()
    List = List.split(" ")
    list1 = []
    list2 = []
    for i in range(len(List)):
        if int(List[i]) >= 0:
            list1.append(int(List[i]))
        else:
            list2.append(int(List[i]))
    return sum(list1) - sum(list2)
print(Partition())