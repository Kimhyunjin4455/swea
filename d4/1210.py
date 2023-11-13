# T = 10
# for test_case in range(1, T+1):
#     n = int(input())
#     size = 100
#     area = [list(map(int, input().split())) for i in range(size)] # 1: 사다리, 0: 여백, 2: 도착지점
#     end_row = 99
#     end_column = 0
#     for j in range(100):
#         if area[99][j] == 2:
#             end_column = j # 마지막 행의 도착지점을 찾음, end_column은 99
#
#     while end_row != 0:
#         if 0 <= end_column+1 <= 99 and area[end_row][end_column+1]: # 오른쪽이 1이면 오른쪽에 0이 나올 때까지 위로 한 칸 이동
#             while end_column + 1 <= 99 and area[end_row][end_column+1]:
#                 end_column +=1
#             end_row -=1 # 위로 이동하기에 row값 감소
#         elif 0 <= end_column-1 <= 99 and area[end_row][end_column-1]: # 왼쪽이 1이면 왼쪽에 0이 나올때까지 위로 한 칸 이뎡이동
#             while 0 <= end_column-1 and area[end_row][end_column-1]:
#                 end_column-=1
#             end_row-=1
#         else: # 없으면 위로 올라가기
#             end_row -= 1
#     print("#{} {}".format(test_case, end_column))

# 위에서 아래로
T = 10
for test_case in range(1, T+1):
    n = int(input())
    area = [list(map(int, input().split())) for i in range(100)]

    dr = [1,0,0] # 아래, 오른쪽, 왼쪽
    dc = [0,1,-1]

    result = 0
    for i in range(100):
        if area[0][i]: # 시작점 찾기
            row, column = 0,i
            d = 0
            while row < 99:
                if d == 0:
                    if column > 0 and area[row][column-1]: # 왼쪽으로 갈 수 있을 때 'area[row][column-1]'값이 1
                        d = 2
                    elif column < 99 and area[row][column+1]:
                        d = 1
                else:
                    if area[row+1][column]:
                        d = 0
                row += dr[d]
                column += dc[d]
            if area[row][column] == 2:
                result = i
                break
    print("#{} {}".format(test_case, result))


#RE