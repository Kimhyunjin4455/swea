T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(input())

    isSame = False

    if(N % 2 == 0): # 문자열 길이가 짝수면은 두번 연속해서 가능
        for i in range(N//2):
            if lst[i] == lst[i+(N//2)]: # 두번 연속이기에 2로 나누어 반복되는지 확인
                isSame = True
            else:
                isSame = False
                break # 중요: False일때는 바로 탈출해야 True로 변경되지 않음
    else: # 문자열 길이가 홀수인 경우에는 같을 수가 없음
        isSame = False

    if isSame == False:
        print("#{} No".format(test_case))
    else:
        print("#{} Yes".format(test_case))


