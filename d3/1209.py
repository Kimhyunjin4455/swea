# 다시 풀기 hint 행/열/대각선을 각각 반복을 통해 계산
T = 10
for test_case in range(1, T+1):
    test_num = int(input())
    num_array = []
    limited_size = 100
    for i in range(limited_size):
        num_list = list(map(int, input().split())) # n개의 숫자 입력 후 분리
        num_array.append(num_list)
    result = 0 # 최종 결과값
    result_row = 0
    result_row_now = 0 # 매 반복마다 현재의 합계를 구해 기존의 최댓값과 비교를 위한 용도
    result_column = 0
    result_column_now = 0
    result_cross_A = 0
    result_cross_B = 0

    for i in range(limited_size):
        for j in range(limited_size):
            result_row_now += num_array[i][j] # 가로의 합
            result_column_now += num_array[j][0] # 세로의 합

        result_row = max(result_row_now, result_row)
        result_row_now = 0

        result_column = max(result_column_now, result_column)
        result_column_now = 0

        result_cross_A += num_array[i][i]
        result_cross_B += num_array[i][limited_size-i-1]

    result = max(result_row, result_column, result_cross_A, result_cross_B)

    print("#{} {}".format(test_case, result))