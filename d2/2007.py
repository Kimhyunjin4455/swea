T = int(input())
for tc in range(1,T+1):
    pattern = list(map(str, list(input())))

    for i in range(29):
        for j in range(i+1, 30):
            if pattern[i] == pattern[j]:
                if pattern[:j] == pattern[j:j*2]:
                    print("#{} {}".format(tc, j))
                    break
                else:
                    continue
        break


