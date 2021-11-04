def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    import copy
    temp = [points[0]]
    max = 1
    real_max = 0
    for i in range(1,len(points)):
        temp_points = copy.deepcopy(points)
        temp_points.remove(temp[0])
        try:
            k = (temp[0][1] - points[i][1])/(temp[0][0] - points[i][0])
            for j in range(0, len(temp_points)):
                try:
                    t = (temp[0][1] - temp_points[j][1]) / (temp[0][0] - temp_points[j][0])
                    if t == k:
                        max = max + 1
                except:
                    continue
        except:
            k = temp[0][0]
            for j in range(0, len(temp_points)):
                t = temp_points[j][0]
                if t == k:
                    max = max + 1
        if max >= real_max:
            real_max = max
        max = 1
        temp = [points[i]]
    print(real_max)

maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]])