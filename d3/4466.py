# N개의 과목에 대한 시험
# 점수는 정수, 100점 만점
# 성적표에 k개 입력 가능, 성적표에 나타나는 총점 가장 크도록

T = int(input())
for test_case in range(1, T+1):
    n,k = map(int, input().split())
    grade_card = []
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)

    for i in range(k):
        grade_card.append(scores[i])

    print("#{} {}".format(test_case, sum(grade_card)))


