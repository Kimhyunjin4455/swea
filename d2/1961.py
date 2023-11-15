T = int(input())

def rotate(area, n):
    left_up = area[0][0]
    right_up = area[0][n-1]
    right_down = area[n-1][n-1]
    left_down = area[n-1][0]
    rotated_ary = [[0] * n for _ in range(n)]
    for i in range(len(area)):
        for j in range(len(area)):
        # (0,0)<(5,0) (0,1)<(4,0) (0,5)<(0,0) (5,5)<(0,5) (0,4)<(1,0) (1,4)<(1,1) (2,4)<(1,2)
            rotated_ary[i][j] = area[n-j-1][i]

    return rotated_ary



for test_case in range(1,T+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]



    rot_90 = rotate(area,n)
    rot_180 = rotate(rot_90,n)
    rot_270 = rotate(rot_180,n)



    print("#{}".format(test_case))
    # 배열을 90/180/270도 회전한 방향
    for i in range(n):
        print(*rot_90[i], sep='', end=' ')
        print(*rot_180[i], sep='' ,end=' ')
        print(*rot_270[i], sep='')




# ex
# 1 2 3   7 4 1 ->
# 4 5 6   8 5 2
# 7 8 9   9 6 3
# #1
# 741 987 369
# 852 654 258
# 963 321 147