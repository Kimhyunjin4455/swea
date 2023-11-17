T = int(input())
for i in range(1,T+1):
    if (str(i).count('3') == 0 and str(i).count('6') == 0 and str(i).count('9') == 0 ):
        print(i, end= ' ')
    else:
        print('-' * (str(i).count('3') + str(i).count('6') + str(i).count('9')), end=' ')
