# # T = int(input())
# # def dfs(col, row, area, result):
# #     dc = [-1, 1, 0, 0]
# #     dr = [0, 0, -1, 1]
# #     dir = [0, 1, 2, 3]  # 상 하 좌 우
# #
# #
# #     # 7자리 생성을 위한 반복
# #     if len(result) == 7:
# #         return int("".join(map(str, result)))
# #         # 각 방향을 돌며
# #     for d in range(4):
# #         # 이동 가능한 범위를 벗어난다면
# #         if (col + dc[dir[d]]) < 0 or (col + dc[dir[d]]) >= 4 or (row + dr[dir[d]]) < 0 or (row + dr[dir[d]]) >= 4:
# #             continue
# #         else:
# #             nc = col +dc[dir[d]]
# #             nr = row +dr[dir[d]]
# #             result.append(area[col][row])
# #             dfs(nc,nr,area,result)
# #
# #
# # for tc in range(1, T+1):
# #     area = [list(map(int, input().split())) for _ in range(4)]
# #     dc = [-1,1,0,0]
# #     dr = [0,0,-1,1]
# #     dir = [0,1,2,3] # 상 하 좌 우
# #     result = []
# #     final_result = []
# #
# #     # 모든 좌표에 대해
# #     for col in range(4):
# #         for row in range(4):
# #             final_result.append(dfs(col, row, area, result))
# #
# #     print("#{} {}".format(tc, len(set(final_result))))
# #
# #
# #
# #
#
#
# def dfs(number, x, y):
#     # 길이가 7이 되면 result에 값을 추가하고 break
#     if len(number) == 7:
#         result.add(number)
#         return
#
#     # 상하좌우 4방향을 탐색
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         # 리스트의 범위를 벗어나지 않으면
#         if 0 <= nx < 4 and 0 <= ny < 4:
#             # number에 값을 붙여주고 다음 지점으로 이동하여 재귀탐색
#             dfs(number + maps[x][y], nx, ny)
#
#
#
#
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# for tc in range(1, 1 + int(input())):
#     maps = [input().split() for _ in range(4)]
#
#     # 중복이 없기 때문에 set을 사용했다.
#     result = set()
#     # 시작 지점을 선택
#     for i in range(4):
#         for j in range(4):
#             dfs('', i, j)
#     print('#{} {}'.format(tc, len(result)))

def dfs(row, col, num, result):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    if len(num) == 7:
        result.add(num)
        return result
    num += str(area[row][col])

    for dir in range(4):
        if row + dr[dir] < 0 or row + dr[dir] >= 4 or col + dc[dir] < 0 or col + dc[dir] >= 4:
            continue
        dfs(row + dr[dir], col + dc[dir], num, result)

T = int(input())
for tc in range(1, T+1):
    area = [list(map(int, input().split())) for _ in range(4)]
    result = set()

    for row in range(4):
        for col in range(4):
            num = ""
            dfs(row, col, num, result)

    print("#{} {}".format(tc, len(result)))


