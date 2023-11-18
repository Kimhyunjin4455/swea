# 무한히 많은 행과 열이 있는 곱셈표
# (i, j)셀에는 정수 ixj
# 현재 당신의 위치는 셀 (1, 1)
# 오른쪽이나 아래쪽 방향으로 이동 ( 당신이 (i, j)에 서 있다면, (i+1, j)나 (i, j+1)로 이동 )
# 정수 N이 주어질 때, N이 적혀 있는 어떤 셀에 도착하기 위해서 최소 몇 번 움직
# 2 <= N <= 10^12)
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = []

    for i in range(1, int(N**0.5)+1): # N+1이 아닌 int(N ** 0.5) 로 두어야 함
        if N % i == 0:
            result.append((i-1) + (N // i) - 1 )
            # (1, 1)에서 (i, j)까지 가는 횟수 : (i - 1) + (N // i - 1)
            #  (i, j) = (i, N // i)

    print("#{} {}".format(test_case, min(result)))
