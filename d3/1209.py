# 다시 풀기 hint 행/열/대각선을 각각 반복을 통해 계산
T = 10
for test_case in range(1, T+1):
    size_limit = 100
    test_num = int(input())
    num_array = []
    for i in range(size_limit):
        num_array.append(list(map(int, input().split())))

    result = 0
    result_row = 0
    result_column = 0
    result_cross_a = 0
    result_cross_b = 0

    for i in range(size_limit): # 열의 합
        for j in range(size_limit):
            result += num_array[i][j]
        result_row = max(result, result_row)
        result = 0

    for i in range(size_limit): # 행의 합
        for j in range(size_limit):
            result += num_array[j][i]
        result_column = max(result, result_column)
        result = 0

    for i in range(size_limit):
        result_cross_a += num_array[i][i]

    for i in range(size_limit):
        result_cross_b += num_array[i][size_limit-i-1]

    result = max(result_row, result_column, result_cross_a, result_cross_b)

    print("#{} {}".format(test_case, result))