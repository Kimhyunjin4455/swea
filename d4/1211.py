T = 10
for test_case in range(1,T+1):
    n = int(input())
    size = 100
    area = [list(map(int, input().split())) for i in range(size)]

    min_count = 1e9
    result = 0
    for i in range(size):
        if area[0][i] == 1:
            row = 0
            column = i
            cnt = 0
            while row != size-1:
                row += 1
                cnt += 1
                if 0 < column and area[row][column-1]:  # 왼쪽으로 이동 가능하다면
                    while 0 < column and area[row][column-1]:  # 왼쪽에 0이 나올때까지
                        column -= 1  # 왼쪽으로 이동
                        cnt += 1
                elif column < size-1 and area[row][column+1]:  # 오른쪽으로 이동 가능하다면
                    while column < size-1 and area[row][column+1]:  # 오른쪽으로 이동
                        column += 1
                        cnt += 1

            if min_count > cnt:
                min_count = cnt
                result = i
    print("#{} {}".format(test_case, result))

