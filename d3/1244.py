# 보너스 상금
# 우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환
# ex: 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회
# 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번
# 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
# 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액

# def dfs(n):
#     global ans
#     if n == N:
#         ans = max(ans, int("".join(map(str,lst)))) #
#         return
#
#     # L개에서 2개뽑는 모든 조합
#     for i in range(L-1):
#         for j in range(i+1, L):
#             lst[i], lst[j] = lst[j], lst[i]
#
#             chk = int("".join(map(str,lst)))
#             if (n, chk) not in v: # 사용하지 않은 조합
#                 dfs(n+1)
#                 v.append((n,chk))
#
#             lst[i], lst[j] = lst[j], lst[i]
#
# T = int(input())
# for i in range(1,T+1):
#     money, chance = input().split()
#     N = int(chance) # 횟수
#     lst = []
#     for num in money:
#         lst.append(int(num))
#     L = len(lst)
#     ans = 0 # 비교 후 최댓값이 필요하기에 0으로 처리
#     v = []
#     dfs(0)
#     print("#{} {}".format(i, ans))

#
# def dfs(n):
#     global result
#     if n == limit:
#         result = max(result, int("".join(map(str, num_list))))
#
#     for i in range(L-1):
#         for j in range(i+1, L):
#             num_list[i], num_list[j] = num_list[j], num_list[i]
#             visited = int("".join(map(str, num_list)))
#
#             if(n, visited) not in v:
#                 dfs(n+1)
#                 v.append((n, visited))
#
#             num_list[i], num_list[j] = num_list[j], num_list[i]
#
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     number, chance = input().split()
#     limit = int(chance)
#     num_list = []
#
#     for num in number:
#         num_list.append(num)
#     L = len(num_list)
#     result = 0
#     v= []
#
#     dfs(0)
#     print("#{} {}".format(test_case, result))
#
# re resolve

def dfs(n):
    global result
    if n == end:  # 횟수만큼 비교했다면 가장 큰 값 받기
        result = max(result, int("".join(num_list)))
        return # 최댓값을 찾았기에 종료

    for i in range(num_length-1):
        for j in range(i+1, num_length):
            num_list[i], num_list[j] = num_list[j], num_list[i]  # 특정 인덱스끼리 변경해줌
            # dfs(n+1) # 새로운(값 변경된) num_list 이용해서 가지치기
            # 방문된 값이라면 더 할 필요가 없음(문제의 제약사항 지키기)
            visited = int("".join(num_list))
            if(n, visited) not in v:  # '튜플'이 리스트 안에 존재하지 않는다면(방문한 값이 아니라면)
                dfs(n+1)  # 탐색 진행
                v.append((n, visited))  # 튜플 방문 처리
            num_list[i], num_list[j] = num_list[j], num_list[i]  # 그 다음 반복을 위해 원상복구



T = int(input())
for test_case in range(1, T+1):
    number, chance = input().split()  # 값과 기회 입력받고
    end = int(chance)  # 정수 형변환
    num_list = []
    for num in number:
        num_list.append(num)  # 리스트를 통해서 값 분리
    num_length = len(number)  # 반복을 위해 구해야 함
    #print(num_length)

    print(type(num))

    result = 0
    v = []
    dfs(0)  # 0회 부터 시작
    print("#{} {}".format(test_case, result))

















