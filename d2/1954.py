T = int(input())
for test_case in range(1, T+1):
    n = int(input()) # 크기
    area = [[0] * n for _ in range(n)] # 달팽이 모양, 2차원

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    now_dir = 0
    row = 0
    column = 0

    for i in range(1, (n*n)+1):
        area[row][column] = i
        row += dr[now_dir]
        column += dc[now_dir]

        if row < 0 or column <0 or row >= n or column >=n or area[row][column] != 0: # 최대 길이거나 값이 입력되어 있는 상태면
            row -= dr[now_dir]
            column -= dc[now_dir]

            now_dir = (now_dir+1) % 4 # 4부터는 dr/dc의 범위를 초과하기에 %4
            row += dr[now_dir]
            column += dc[now_dir]

    print("#{}".format(test_case))
    for ary in area:
        print(*ary)







    # 열이 끝까지 커지고(값이 0이 아닐때까지), 값 넣고 num+1
    # 행이 끝까지 커지고(..), ..
    # 열이 끝까지 작아지고(..), ..
    # 행이 끝까지 작아지고(











