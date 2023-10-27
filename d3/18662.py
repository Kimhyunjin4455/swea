T = 3
for i in range(1,T+1):
    a, b, c = map(int, input().split())
    left = b - a
    right = c - b
    if left == right:
        print(f'#{i} {0.0}')
    else:
        #print(f"#{i} {abs(right - left) / 2:.1f}")
        print("#{} {:.1f}".format(i, abs(right - left) / 2))
# 중간의 수가 크다면 차이만큼 빼고, 작으면 더해서 등차수열을 이루게 함

