global count
count = 0


def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    global count
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                count = count + 1
    while count != 0:
        print(count)
        for i in range(1,10):
            board = solution2(board, i)
        print(count)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    board = solution(board, i, j)


def solution2(board, a):
    row = []
    line = []
    for i in range(9):
        for k in range(9):
            if board[i][k] == str(a):
                row.append(k)
                line.append(i)
    b = []
    for i in range(9):
        for k in range(9):
            if board[i][k] == "." and i not in line and k not in row:
                b.append([i, k])
    result = []
    for item in b:
        if str(a) not in board[item[0]]:
            temp = []
            for t in range(9):
                temp.append(board[t][item[1]])
            if str(a) not in temp:
                temp2 = []
                count2 = 0
                for t in range(3 * (item[0] // 3), 3 * (item[0] // 3) + 3):
                    for q in range(3 * (item[1] // 3), 3 * (item[1] // 3) + 3):
                        temp2.append(board[t][q])
                        for item2 in b:
                            if item2 == [t, q]:
                                count2 = count2 + 1
                if str(a) not in temp2 and count2 == 1:
                    result.append(item)
                    print(item)
    for item3 in result:
        board[item3[0]][item3[1]] = str(a)
        global count
        count = count - 1
    return board

def solution(board, i, j):
    a = []
    for k in range(1, 10):
        if str(k) not in board[i]:
            temp = []
            for t in range(9):
                temp.append(board[t][j])
            if str(k) not in temp:
                temp2 = []
                for t in range(3 * (i // 3), 3 * (i // 3) + 3):
                    for q in range(3 * (j // 3), 3 * (j // 3) + 3):
                        temp2.append(board[t][q])
                if str(k) not in temp2:
                    a.append(str(k))
    if len(a) == 1:
        global count
        board[i][j] = a[0]
        count = count - 1
        return board
    else:
        return board


solveSudoku([[".", ".", "9", "7", "4", "8", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."],
             [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]])

# solution2([["5", "3", ".", ".", "7", ".", ".", ".", "."],
#            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#            [".", "9", "8", ".", ".", ".", ".", "6", "."],
#            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#            [".", "6", ".", ".", ".", ".", "2", "8", "."],
#            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#            [".", ".", ".", ".", "8", ".", ".", "7", "9"]], 8)
