# for t in range(1,11):
#     n = int(input())
#     building = list(map(int, input().split()))
#     total = 0
#
#     for i in range(2, n-2): # ex: 100개의 빌딩이 있을때 98번째 빌딩까지가 100번째와 비교 가능
#         sub1 = building[i] - building[i - 2]
#         sub2 = building[i] - building[i - 1]
#         sub3 = building[i] - building[i + 1]
#         sub4 = building[i] - building[i + 2]
#         if(sub1 > 0 and sub2 > 0 and sub3 > 0 and sub4 > 0):
#             total += min(sub1, sub2, sub3, sub4)
#
#     print("#{} {}".format(t, total))

#re Resolve
# 테스트 케이스 10회 진행
T = 10
for i in range(1,T+1):
    n = int(input()) # 건물의 갯수
    building = list(map(int, input().split())) # 건물의 높이 입력받기
    total = 0 # 조건에 부합하는 층(결과값)

    for i in range(2, n-2): # 가장 오른쪽/왼쪽 두개의 건물 높이는 0으로 입력받기에
        view1 = building[i] - building[i-2]
        view2 = building[i] - building[i-1]
        view3 = building[i] - building[i+1]
        view4 = building[i] - building[i+2]

        if(view1 > 0 and view2 > 0 and view3 > 0 and view4 > 0): #양옆으로의 전망이 확보된다면
            total += min(view1, view2, view3, view4)

    print(total)























