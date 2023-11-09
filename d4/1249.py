from collections import deque

T = int(input())
for test_case in range(1,T+1):
    size = int(input())
    # area = []
    #
    # for i in range(size):
    #     area.append(list(map(int, input().split())))
    area = [list(map(int, list(input()))) for _ in range(size)]
    visit = [[1000000] * size for i in range(size)]  # 방문 리스트 생성
    dx = [0, 0, -1, 1] # 상하좌우
    dy = [-1, 1, 0 ,0]



    def bfs(deq, visit):
        while deq:
            (x,y,sums) = deq.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= size or ny >= size or (nx, ny) == (0, 0) or visit[nx][ny] <= area[nx][ny] + sums:
                    continue

                visit[nx][ny] = area[nx][ny] + sums
                deq.append((nx, ny, visit[nx][ny]))
        return visit[-1][-1]


    deq = deque()
    deq.append((0, 1, area[0][1]))
    deq.append((1, 0, area[1][0]))

    print("#{} {}".format(test_case, bfs(deq,visit)))



