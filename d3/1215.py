T = 10
for test_case in range(1, T+1):
    length = int(input()) #  찾아야 하는 회문의 길이
    board = [list(map(str,list(input()))) for _ in range(8)]
    result = 0

    for row in range(8):
        for column in range(8-length+1): # column 값은 0일 때 부터 8-length때까지
            r = board[row][column:column + length] # 2차원 배열의 인덱스는 column 부터 column + length 이전까지
            if r == r[::-1]:
                result += 1

    for row in range(8-length+1):
        for column in range(8):
            r='' # column(세로 기준으로) 값 바뀔때 초기화 필요
            for z in range(length):
                r += board[row+z][column]
            if r == r[::-1]:
                result+=1
    print("#{} {}".format(test_case, result))