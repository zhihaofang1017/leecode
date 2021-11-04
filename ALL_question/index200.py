def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    for i in range(len(grid)):
        grid[i].append("0")
        grid[i].insert(0, "0")
    R = ["0"] * (len(grid[0]))
    grid.append(R)
    grid.insert(0, R)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                grid = solution(grid,i,j)
                count = count + 1
    return count


def solution(grid, i, j):
    temp = [(i, j)]
    total = [(i, j)]
    count = 0
    while count != len(total):
        count = len(total)
        temp2 = []
        for item in temp:
            if grid[item[0] - 1][item[1]] == "1" and (item[0] - 1, item[1]) not in total:
                total.append((item[0] - 1, item[1]))
                temp2.append((item[0] - 1, item[1]))
            if grid[item[0] + 1][item[1]] == "1" and (item[0] + 1, item[1]) not in total:
                total.append((item[0] + 1, item[1]))
                temp2.append((item[0] + 1, item[1]))
            if grid[item[0]][item[1] - 1] == "1" and (item[0], item[1] - 1) not in total:
                total.append((item[0], item[1] - 1))
                temp2.append((item[0], item[1] - 1))
            if grid[item[0]][item[1] + 1] == "1" and (item[0], item[1] + 1) not in total:
                total.append((item[0], item[1] + 1))
                temp2.append((item[0], item[1] + 1))
        temp = temp2
    for item in total:
        grid[item[0]][item[1]] = "2"
    return grid

numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
