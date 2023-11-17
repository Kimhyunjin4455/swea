# 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 하루에 최대 1만큼 구입할 수 있다.
# 판매는 얼마든지 할 수 있다.

T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    price = list(map(int, input().split()))
    cnt = 0
    now = 0

    max_num = price[size-1]
    for i in range(size-1, 0,-1):
        if price[i] > max_num:
            max_num = price[i]
        cnt += (max_num-price[i])

    if price[0] <= max_num:
        cnt += (max_num-price[0])

    if cnt <= 0:
        cnt = 0

    print("#{} {}".format(test_case, cnt))

    # 처음부터 계속 하락하면 0
    # 마지막이 제일 크면 (마지막*이전까지의 갯수) - 이전까지 구매한 돈의 합
    # 중간이 제일 크면





