T = int(input())
for test_case in range(1,T+1):
    A,B = map(int, input().split())
    if A == B:
        gcd = A
    else: # 연속된 자연수를 요구하기에 gcd는 1이 될 수 밖에 없음
        gcd = 1
    print("#{} {}".format(test_case, gcd))