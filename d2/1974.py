T = int(input())
for test_case in range(1, T+1):
    area = [list(map(int, input().split())) for _ in range(9)]
    # 가로가 전부 다른지
    # 세로가 전부 다른지
    # 가로 3칸/세로3칸이 다른지 끝나면 가로,세로 +3

    col_cnt = 0
    row_cnt = 0
    cross_cnt = 0
    cross_set = set()
    row_set = set()
    result_cnt = 0

    for i in range(9):
        if len(set(area[i])) == 9:
            col_cnt += 1
    if col_cnt == 9:
        result_cnt += 1

    for i in range(9):
        for j in range(9):
            row_set.add(area[j][i])
        if len(row_set) == 9:
            row_cnt += 1
            row_set = set() # 다음 세로 열의 집합 생성을 위해 빈값으로 초기화
    if row_cnt == 9:
        result_cnt += 1

    for size_row in range(0,7,3): # 첫칸부터 세칸씩 보면서(6까지만 증가하면 되기때문에 7로 기준을 잡음)
        for size_col in range(0,7,3):
            for k in range(size_row, size_row+3):
                for l in range(size_col,size_col+3):
                    cross_set.add(area[k][l])
            if len(cross_set) == 9:
                cross_cnt += 1
                cross_set = set() # 다음 구역의 집합 생성을 위해 빈값으로 초기화

    if cross_cnt == 9:
        result_cnt += 1

    if result_cnt == 3:
        print("#{} {}".format(test_case, 1))
    else:
        print("#{} {}".format(test_case, 0))