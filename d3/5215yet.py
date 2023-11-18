# 햄버거 재료에 대한 점수와 가게에서 제공하는 재료에 대한 칼로리가 주어짐
# 정해진 칼로리 이하의 조합 중에서 가장 선호하는 햄버거를 조합 (같은 재료를 여러 번 사용 가능)
# 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합

def dfs(start, score, calrorie):
    global best
    if calrorie > L:
        return
    if calrorie <= L:
        if best < score:
            best = score
    for j in range(start, N):
        dfs(j+1, score + foods_info[j][0], calrorie + foods_info[j][1])



T = int(input())
for test_case in range(1,T+1):
    N, L = map(int, input().split()) # 재료의 수 / 전체 칼로리
    best = 0

    foods_info = [list(map(int, input().split())) for _ in range(N)]
    dfs(0,0,0)


    print("#{} {}".format(test_case, best))







    # print("#{} {}".format(test_case, max(result_score)))



