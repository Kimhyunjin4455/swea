# 농작물의 가치는 0~5
# 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    area = [list(map(int, input())) for _ in range(n)]
    result = 0
    # 1번 예시 23이지만 22로 구해짐
    for i in range(n//2+1):
        result += area[i][n // 2] # 0+2+5+4+0+3+2+2+0
        # print(result)
        now = i
        # 0-0 1-2 2-4 n//2까지는 그 값의 두배씩 양옆의 인덱스값이 더해지고 n//2보다 커지면 n-1 인덱스까지 다시 -2씩 줄어듬
        if now > 0: # 두번째부터 중간까지 적용
            for k in range(1,now+1):
                result += area[now][n//2+k]
                result += area[now][n//2-k]
                # print(result)
    for j in range(n-1, n//2, -1): # 2+0+1
        result += area[j][n // 2]
        # print(result)
        now = j
        if now < n-1:
            for l in range(0,n-now-1): # 이 구간에서 시작점을 1로 설정하면 반복이 되지 않음
                result += area[now][n//2 + (l+1)]
                result += area[now][n//2 - (l+1)]
        # 양옆의 값을 더함(더하는 갯수를 줄여가면서)
        #     print(result)


    print("#{} {}".format(test_case, result))

