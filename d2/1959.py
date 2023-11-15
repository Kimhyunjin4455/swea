T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    value = 0
    mini_ary_size = min(n,m)
    move_limit = abs(n-m)
    for i in range(move_limit+1): # 양 리스트의 크기 차이 범위 내에서 움직일 수 있음 (두 배열의 길이 차이 + 1만큼 반복)
        value = 0
        for j in range(mini_ary_size): # 작은 배열의 인덱스는 j 큰 배열의 인덱스는 j에다가 i 값을 더해가며 반복
            if n == m:
                value += A[j] * B[j]
            if n < m:
                value += A[j] * B[j+i]
            if n > m:
                value += A[i+j] * B[j]

        if result < value:
            result = value

            # 만약 곱의 값이 현재값 보다 크다면 그 값으로 갱신
    print("#{} {}".format(test_case, result))

