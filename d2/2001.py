T = int(input())
for test_case in range(1,T+1):
    n,m = map(int, input().split())
    area = []
    max_result = 0
    for i in range(n):
        area.append(list(map(int, input().split())))

    for start_value_column in range(n-m+1):
        for start_value_row in range(n-m+1):
            result = 0
            for i in range(start_value_column, start_value_column +m):
                for j in range(start_value_row, start_value_row +m):
                    result += area[i][j]
                if(result > max_result):
                    max_result = result
    print("#{} {}".format(test_case, max_result))