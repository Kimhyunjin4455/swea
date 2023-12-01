import sys
from collections import deque

# input = sys.stdin.readline()

def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        r,c = queue.popleft()
        visited[r][c] = True

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0<=nr<16 and 0<=nc<16 and visited[nr][nc] == False:
                if area[nr][nc] == 0:
                    queue.append((nr,nc))
            if nr == end_row and nc == end_col:
                return True
    return False




dr = [-1,1,0,0]
dc = [0,0,-1,1]
T = 10
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, list(input())))for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    # 시작점 설정
    for i in range(16):
        for j in range(16):
            if area[i][j] == 2:
                row = i
                col = j

    # 끝점 설정
    for i in range(16):
        for j in range(16):
            if area[i][j] == 3:
                end_row = i
                end_col = j


    if(bfs(row, col) == True):
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))







