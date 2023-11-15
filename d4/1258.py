# 빈 용기는 0, 화학 물질 들어있는 용기는 종류에 따라 1~9정수
# 화학 물질이 담긴 용기들이 사각형을 이루고 있다. 또한, 사각형 내부에는 빈 용기가 없다.
# 화학 물질이 담긴 용기들로 이루어진 사각형들은 각각 차원(가로의 용기 수 x 세로의 용기 수)이 다르다.
# area 사이즈는 100이하

def matrix(x,y):
    i,j = x,y
    row = 1
    column = 1

    while True:
        x += 1 # x값에 따라 행값이 변경됨 (실세계의 가로 세로와 반대로 생각)
        if x < size and area[x][y] != 0 and visited[x][y] == False:
            row +=1
        else:
            x-=1 # x값 원복
            break
    while True:
        y += 1
        if y < size and area[x][y] != 0 and visited[x][y] == False:
            column += 1
        else:
            y -= 1
            break
    for k in range(i, x+1):
        for l in range(j, y+1):
            visited[k][l] = True

    return [row, column]


T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    area = [list(map(int, input().split())) for _ in range(size)]
    visited = [[False] * size for _ in range(size)]
    result = []

    for i in range(size):
        for j in range(size):
            if area[i][j] != 0 and visited[i][j] == False:
                value = matrix(i,j)
                result.append(value)

    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    print("#{} {}".format(test_case, len(result)), end=' ')
    for r in result:
        print(*r, end=' ')
    print()

# lst = ["x", "y", "z"]
# print(*lst, sep=",")
# Python의*연산자를 사용하여 객체의 압축을 풀 수 있음
# x,y,z
# print(*lst, sep='')
# xyz

# 주어진 행렬에서 추출된 부분 행렬들을 개수
# 행렬들의 행과 열의 크기 (크기가 작은 순서대로 출력, 크기가 같을 경우 행이 작은 순으로 출력)
# 행 row 열 column



