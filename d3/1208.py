# 높은 곳의 상자를 낮은 곳에 옮기는 방식
# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내
# 상자를 옮기는 작업 횟수에 제한 -> 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
# 가로 길이는 항상 100, 모든 위치에서 상자의 높이는 1이상 100이하, 덤프 횟수는 1이상 1000이하

T = 10
for test_case in range(1,T+1):
    dump = int(input())
    box_height = list(map(int, input().split()))
    box_height.sort() # 정렬
    result = 0
    for i in range(dump): # 덤프 횟수 만큼
        # 정렬된 리스트에서 마지막 인덱스 값 하나 줄이고 첫번째 인덱스 값 하나 늘리고 다시 정렬
        box_height[len(box_height)-1] -= 1
        box_height[0] += 1
        box_height.sort()
    result = box_height[len(box_height)-1] - box_height[0]
    print("#{} {}".format(test_case,result))