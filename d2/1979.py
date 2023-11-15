# N X N 크기의 단어 퍼즐
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력

# k개 보다 길면 x

T = int(input())
for test_case in range(1,T+1):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if area[i][j] ==1:
                cnt += 1
            if area[i][j] ==0 or j == n-1: # 0 만나거나 끝점 도달시
                if cnt == k: # 조건 만족하면
                    result += 1
                if area[i][j] == 0: # 0의 경우
                    cnt = 0 # 다시 세기 위해 0으로 초기화

    for i in range(n):
        cnt = 0
        for j in range(n):
            if area[j][i] == 1:
                cnt += 1
            if area[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                if area[j][i] == 0:
                    cnt = 0


    print("#{} {}".format(test_case, result))




