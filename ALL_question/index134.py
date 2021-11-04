def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    data2 = []
    judge = 0
    for i in range(len(gas)):
        data2.append(gas[i] - cost[i])
        judge = judge + (gas[i] - cost[i])
    if judge < 0:
        return -1
    temp = 0
    index = 0
    for i in range(len(data2)):
        if temp >= 0:
            temp = temp + data2[i]
        else:
            temp = data2[i]
            index = i
        print(index)

    print(data2)
canCompleteCircuit([-2,2,-3,4,5],[0,0,0,0,0])
canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
canCompleteCircuit([2,3,4],[3,4,3])