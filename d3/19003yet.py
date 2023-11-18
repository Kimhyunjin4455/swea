# # 양의 정수 N, 그리고 N 개의 길이가 같은 문자열
# # 이들 중 몇 개의 문자열을 고른 후, 고른 문자열들을 적당히 재배열 (문자열을 재배열하는 것이고, 문자열 내부 문자의 순서는 바꿀 수 없다)
# # 순서대로 합쳤을 때 팰린드롬이 되게, 최종 팰린드롬의 길이를 최대화
# T = int(input())
# for test_case in range(1, T+1):
#     n,m = map(int, input().split())
#     chr_ary = list(map(str, list(input() for _ in range(n))))
#
#
#     result = 0
#     now = ''
#     max_result = 0
#
#     for i in range(len(chr_ary)):
#         res = ''
#         for j in range(len(chr_ary)):
#             if i == j:
#                 continue
#             if now == '':
#                 now += chr_ary[i]
#             res = now + chr_ary[j] # abcdedcba
#
#             if res == res[::-1]:
#                 if len(res) > max_result:
#                     result = len(res)
#                     max_result = len(res)
#
#             now = res
#
#     if result == 0:
#         result_arr = []
#         for s in chr_ary:
#             if s == s[::-1]:
#                 result_arr.append(len(s))
#         if len(result_arr) == 0:
#             result = 0
#         else:
#             result = max(result_arr)
#
#
#
#     print("#{} {}".format(test_case, result))
#


# 뒤집었을 때 같은 문자열의 길이 + 펠린드롬인 문자열 1개 (없으면 제외) 한 길이가 답
# 조건1: 문자열이 들어왔을 때, 펠린드롬이 2개 이상이면 1개만 사용 가능 -> 펠린드롬이 연속이면 펠린드롬 규칙 성립하지 않음
# 조건2: 펠린드롬이 아닌 것들을 모아놨을 때, 그 중에 반대로 뒤집었을 때 맞는 것이 없으면 빼도 됨
# 펠린드롬을 모아놓은 리스트를 A, 아닌 것을 모아놓은 리스트를 B라고 할 때, 어차피 A는 많아도 하나만 사용이 가능
# B는 `조건2`를 제외했을 때 남은 것들의 길이와 요소의 개수를 곱함


TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    answer = cnt = 0

    palindrome = False
    isNot = []

    for _ in range(N):
        a = input().rstrip()
        if a != a[::-1]:
            isNot.append(a)
        else:
            palindrome = True

    for _ in range(len(isNot)):
        temp = isNot.pop()
        if temp[::-1] in isNot:
            cnt += 2


    ## 여기까지의 과정을 다 거치면 isNot에는 조건을 충족한 것들만 남고,
    ## palindrome은 True 혹은 False



    # 만약 걸러낸 짝이 'ab', 'ba' 였다면 cnt는 2였을테고, 'abba', 'baab' 둘 다
    # 문자열 길이가 4입니다. ( cnt(2) * M(2) = 4 )
    answer = cnt * M

    # 만약 palindrome이 True라면 가운데 들어갈 수 있겠습니다.
    # 위의 예시대로라면 M은 2였을테니 palindrome이 'cc'였다면 'abccba'가 되겠죠.
    # 어차피 하나만 들어갈 수 있으니 M의 값을 한 번만 추가해줍니다.
    if palindrome:
        answer += M

    print(f'#{tc} {answer}')
