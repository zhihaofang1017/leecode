def Ehab():
    List1 = input()
    List1 = List1.split(" ")
    num_count = int(List1[0])
    times = int(List1[1])
    List2 = input()
    List2 = List2.split(" ")
    List2 = list(map(int,List2))
    List2 = sorted(List2)
    index=0

    for i in range(times):
        if index >= num_count:
            print(0)
        else:
            temp_min = List2[index]
            print(temp_min)

            for j in range(index, num_count):
                List2[j] = List2[j] - temp_min
                if List2[index] == 0:
                    index= index+1



Ehab()