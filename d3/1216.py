#
# def column_len():
#     global count
#     for size in range(100,0,-1): #100부터 1까지
#         for i in range(100): #행
#             for j in range(100): #열
#                 if j + size > 100: #길이의 맞춰 반복하는 값이 넘어서면
#                     break # 반복문 탈출 후 다음 행으로
#                 end = j + size -1
#                 for half in range(j, j+(size//2)): # 절반 반복
#                     if area[i][half] != area[i][end]: # 양쪽에서 검사하고, 다르다면
#                         break
#                     end -= 1
#                 else: # 반복문을 다 돌았다면 회문, for-else구문
#                     count = size
#                     return
# def row_len():
#     global count
#     for size in range(100, 0, -1):  # 100부터 1까지
#         if count >= size: # 열 기준 값보다 작으면 반복은 의미 없음
#             return
#         for i in range(100):
#             if i+size > 100:
#                 break
#             for j in range(100):
#                 end = i + size -1
#                 for half in range(i, i+(size//2)):
#                     if area[half][j] != area[end][j]:
#                         break
#                     end -= 1
#                 else:
#                     count = size
#                     return
#
#
# T = 10
# for test_case in range(1,T+1):
#     n = int(input())
#     area = [list(map(str, input())) for _ in range(100)]
#
#     # 100(최대 길이)부터 점점 짧아지는 식으로 가로의 회문 검사
#     # 세로도 마찬가지, 처음 구한 세로의 값이 가로보다 작다면 가로의 값이 답
#
#     count = 0
#     column_len()
#     row_len()
#
#     print("#{} {}".format(test_case, count))

# 가로(column)에서의 가장 긴 회문과 과 세로(row)에서의 가장 긴 회문 구해서 큰 값 필요
def column_len():
    col_cnt = 0
    # 회문이 길이를 큰 값부터 시작해서 가장 큰 값 구해지는 순간 종료
    for size in range(100,0,-1): # 길이가 점점 줄어들면서
        for i in range(100):
            for j in range(100):
                if j + size > 100: # 회문을 검사하는 범위를 초과
                    break
                end = j + size -1 # 마지막 인덱스 설정
                for half in range(j, j+(size//2)): # 절반만 반복
                    if area[i][half] != area[i][end]:
                        break
                    end -= 1
                else:
                    col_cnt = size
                    return col_cnt

def row_len():
    row_cnt = 0
    for size in range(100,0,-1):
        for i in range(100):
            for j in range(100):
                if i + size > 100:
                    break
                end = i + size - 1 # 각 반복에서의 마지막 인덱스 수식
                for half in range(i,i+(size//2)):
                    if area[half][j] != area[end][j]: # 회문 조건 불만족
                        break
                    end -= 1 # 만족시 길이 줄여가면서 반복
                else: # 회문 조건 달성 시
                    row_cnt = size
                    return row_cnt


T = 10
for test_case in range(1, T+1):
    n = int(input())
    area = [list(map(str, input())) for _ in range(100)]

    result = max(column_len(),row_len())

    print("#{} {}".format(test_case, result))
