T = int(input())

score_arr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T+1):
    N,K = map(int, input().split())
    data = []

    for i in range(N):
        mid, final, assignment = map(int, input().split())
        score_sum = (mid * 0.35) + (final * 0.45) + (assignment * 0.2)
        data.append(score_sum)

    k_score = data[K - 1]
    data.sort(reverse=True)  # 등수를 알기 위해 정렬

     # 0 부터 N-1 까지, K번째 순서는 K-1번째 인덱스
    value = N//10
    final_index = data.index(k_score) // value


    print("#{} {}".format(tc, score_arr[final_index]))
