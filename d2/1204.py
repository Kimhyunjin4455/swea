T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    score = list(map(int, input().split()))
    result = []

    cnt_score = [0] * 101 #점수 등장 횟수, 1차원

    for i in range(len(score)):
        cnt_score[score[i]] += 1

    max_value = max(cnt_score) # 등장 횟수 중 최고 횟수
    for i in range(len(cnt_score)): # 점수별로 반복하면서
        if cnt_score[i] == max_value: # 점수의 등장횟수가 최고 횟수라면
            result.append(i) # 배열에 추가하고



    print("#{} {}".format(test_case, max(result))) # 그중 제일 높은 숫자 출력