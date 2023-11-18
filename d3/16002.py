# 합성수란 (1과 자기 자신 이외)의 다른 자연수들의 곱으로 나타낼 수 있는 자연수
# 예를 들어 1, 3(1*3), 7(1*7), -12(자연수 불가)는 합성수가 아니고, 6, 12, 10000은 합성수
# 자연수 이 주어질 때
# x-y = N 을 만족시키는 10^9이하의 두 합성수 x와 y를 아무거나 하나 구하는 프로그램
# 모든 N에 대해 이 방정식의 해가 존재함을 증명할 수 있다.

# 2<= x, y <= 10^9

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     x, y = N * 9, N * 8 # N*A - N*(A-1) = N(A-A+1) 이용
#     # 자연수 N (1 <= N <= 10^7) -> 2<= x, y <= 10^9 를 만족
#     print("#{} {} {}".format(test_case, x, y))
#
# n = int(input())

# x - y = N은 곧 x = y + N    => y = cnt라면 x = cnt + n
# while문을 통해 cnt, cnt + n이 isPrime인지 확인하고 아니면 출력
def isPrime(num):
    for i in range(2, int(num)): # 소수는 1과 자기 자신외의 수로 나눠지면 안됨
        if num % i == 0:
            return False

    return True


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    cnt = 2 # 함수의 시작점 설정을 위해
    while True:
        if not isPrime(cnt) and not isPrime(cnt + N): #
            print("#{} {} {}".format(test_case, cnt + N, cnt))
            break
        cnt += 1