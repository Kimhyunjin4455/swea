# # T = 10
# # for test_case in range(1,T+1):
# #     n = int(input())
# #     size = 100
# #     area = [list(map(int, input().split())) for i in range(size)]
# #
# #     min_count = 1e9
# #     result = 0
# #     for i in range(size):
# #         if area[0][i] == 1:
# #             row = 0
# #             column = i
# #             cnt = 0
# #             while row != size-1:
# #                 row += 1
# #                 cnt += 1
# #                 if 0 < column and area[row][column-1]:  # 왼쪽으로 이동 가능하다면
# #                     while 0 < column and area[row][column-1]:  # 왼쪽에 0이 나올때까지
# #                         column -= 1  # 왼쪽으로 이동
# #                         cnt += 1
# #                 elif column < size-1 and area[row][column+1]:  # 오른쪽으로 이동 가능하다면
# #                     while column < size-1 and area[row][column+1]:  # 오른쪽으로 이동
# #                         column += 1
# #                         cnt += 1
# #
# #             if min_count > cnt:
# #                 min_count = cnt
# #                 result = i
# #     print("#{} {}".format(test_case, result))
# #
#
#
# T = 10
# for test_case in range(1, T+1):
#     n = int(input())
#     size = 100
#     area = [list(map(int, input().split())) for _ in range(size)]
#     result = 0
#     min_cnt = 100000
#
#
#
#     for c in range(size): # 행마다 값을 체크하며
#         if area[0][c] == 1: # 시작점에 사다리가 있다면
#             column = c # 오른쪽/왼쪽 사다리를 타며 행 값이 변경되기에 따로 변수 생성
#             cnt = 0
#             row = 0 # row 값을 for 바깥에 선언하면 새로운 row 값을 가지고 다음반복을 시작
#             while row != 99: # 마지막 열이 아닌동안
#
#                 row += 1 # 시작점에는 가로로 이어지지 않기에
#                 cnt += 1
#
#                 if column < 99 and area[row][column+1]: # 오른쪽 사다리가 있다면
#                     while column < 99 and area[row][column+1]: # 오른쪽 사다리가 있는동안
#                         column += 1
#                         cnt += 1
#
#                 elif column > 0 and area[row][column-1]:
#                     while column > 0 and area[row][column-1]:
#                         column -= 1
#                         cnt += 1
#
#             if min_cnt > cnt:
#                 min_cnt = cnt
#                 result = c
#
#     print("#{} {}".format(test_case, result))

# '바닥'까지 가장 짧은 이동 거리를 갖는 시작점 x
for test_case in range(10):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(100)]

    lowest_road = 1e9
    result = 0
    # 시작점 설정
    for i in range(100):
        if area[0][i] == 1:
            row = 0
            column = i
            cnt = 0

            while row != 99:
                row+=1
                cnt+=1
                if column + 1 <= 99 and area[row][column+1]:
                    while column + 1 <= 99 and area[row][column+1]:
                        column+=1
                        cnt+=1

                elif column -1 >= 0 and area[row][column-1]:
                    while column - 1 >= 0 and area[row][column-1]:
                        column -=1
                        cnt+=1



            if cnt < lowest_road:
                lowest_road = cnt
                result = i



    print("#{} {}".format(test_case+1, result))
