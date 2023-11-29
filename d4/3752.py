T = int(input())
global result

def scores_cnt(arr):
    arr.insert(0,0)
    arr_sub = arr.copy()
    result = [0]
    for i in range(N+1):
        now = arr[i]
        for j in range(N+1): # 02 23 03 55 25 35
            if i != j:
                now += arr_sub[j]
                if now not in result: # 기존의 값에 존재하지 않아야 추가
                    result.append(now)
                if (arr[i] + arr_sub[j]) not in result:
                    result.append(arr[i] + arr_sub[j])
    return result



for tc in range(1,T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    final = scores_cnt(scores)
    result = []

    print("#{} {}".format(tc,len(final)))



