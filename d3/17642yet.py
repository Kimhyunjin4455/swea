T = int(input())
for test_case in range(1,T+1):
    A,B = map(int, input().split())
    result = 0
    # 값의 차이가 0이면 조작횟수는 0
    # 값의 차이가 2보다 작으면 조작횟수 -1
    # 값의 차이가 짝수면 값의 차이//2
    # 갑의 차이가 홀수면 값의 차이-3 //2 + 1
    if B-A == 0:
        result = 0
    elif B-A <= 1:
        result = -1
    else:
        if (B-A)%2 == 0:
            result = (B-A)//2
        else:
            result = ((B-A-3)//2) + 1

    print("#{} {}".format(test_case, result))


