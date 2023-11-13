# T = 10
# for test_case in range(1,T+1):
#     size = int(input())
#     area = [list(map(int, input().split())) for _ in range(size)]
#     # n극 2, s극 1
#
#     cnt = 0
#     for column in range(size):
#         isN = False
#         for row in range(size): # 열을 기준으로
#             if area[row][column] == 1: # s극일 경우
#                 isN = True
#             if area[row][column] == 2 and isN: # 충돌할때마다 교착 +1
#                 cnt += 1
#                 isN = False
#     print("#{} {}".format(test_case, cnt))
#
#
#
#

T = 10
for test_case in range(1,T+1):
    size = int(input())
    area = [list(map(int, input().split())) for _ in range(size)]

    cnt = 0
    for column in range(size):
        nextN = 0
        for row in range(size):
            if area[row][column] == 1: #s극의 값이면
                nextN = 1
            if area[row][column] == 2 and nextN == 1: # N극이 오고 이전이 s면
                cnt += 1
                nextN = 0

    print("#{} {}".format(test_case, cnt))



