T = int(input())

def dfs(n):
    global ans
    if n == N:
        ans+=1
        return
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] ==0:
            v1[j] = v2[n + j] = v3[n - j] = 1 # 들어갈 수 있는 경우에 전부 넣기
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0



for test_case in range(1, T+1):
    N = int(input())
    ans = 0

    v1,v2,v3 = [[0]*(2*N) for _ in range(3)] # 양 대각선과 같은 row(크기는 N만 되어도 충분하지만 크게 차이 나지 않아 2N으로 길이 설정)에 대해 방문했는지 리스트
    # v1은 같은 행에 대해 열에 놓여진게 있는지
    dfs(0)
    print("#{} {}".format(test_case, ans))