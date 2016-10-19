def print_grid(grid):
    for i in grid:
        print i

def check_knight(x, y):
    return

def check_win_condition(grid):
    white = []
    black = []
    for i in xrange(4):
        for j in xrange(4):
            if grid[i][j] is not None and grid[i][j][1] == 'W':
                white.append((i, j, grid[i][j]))
            if grid[i][j] is not None and grid[i][j][1] == 'B':
                black.append((i, j, grid[i][j][1]))


test_cases = int(raw_input())

for test in xrange(test_cases):
    w, b, m = map(int, raw_input().split())
    l = [[None]*4 for i in xrange(4)]
    for i in xrange(w):
        figure, pos_y, pos_x = raw_input().rstrip().split()
        pos_x = 4 - int(pos_x)
        pos_y = ord(pos_y) - ord('A')
        l[pos_x][pos_y] = (figure, 'W')
    for i in xrange(b):
        figure, pos_y, pos_x = raw_input().rstrip().split()
        pos_x = 4 - int(pos_x)
        pos_y = ord(pos_y) - ord('A')
        l[pos_x][pos_y] = (figure, 'B')

    print_grid(l)