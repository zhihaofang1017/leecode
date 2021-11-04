def Find_Square():
    a = input()
    a = int(a)
    b = input()
    b = int(b)
    square = []
    for i in range(a):
        square1 = input()
        square1 = list(square1)
        square.append(square1)
    size = 1
    BLACK_LIST = []
    for i in range(a):
        for j in range(b):
            if square[i][j] == "B":
                BLACK_LIST.append([i,j])
    all = []
    for i in range(len(BLACK_LIST)):
        while(len(judge(BLACK_LIST,BLACK_LIST[i],size)) > size*size):
            all = judge(BLACK_LIST,BLACK_LIST[i],size)
            size = size + 2
    size = size - 2
    all = all[1:]
    result = all[int((size*size-1)/2)]
    return result[0]+1 and result[1]+1

def judge(BLACK_LIST, position, size):
    all=[position]
    for i in range(size):
        for j in range(size):
            if ([position[0]+i , position[1]+j] in BLACK_LIST):
                all.append([position[0]+i , position[1]+j])
                continue
    return all


print(Find_Square())



