# 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수
# k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수
# 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
# 양의 정수 N 개 A1, …, AN이 주어짐
# 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력
T = int(input())
def check(value):
    value= str(value)
    for i in range(len(value)-1):
        if value[i] > value[i+1]:
            return False
    return True


for test_case in range(1,T+1):
    n = int(input())
    area = list(map(int, input().split()))

    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            value = area[i] * area[j]
            if check(value) :
                result = max(result, value)
        if result == 0:
            result = -1



    print("#{} {}".format(test_case, result))


