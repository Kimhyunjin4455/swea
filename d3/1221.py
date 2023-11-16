T = int(input())
for test_case in range(1, T+1):
    n,m = input().split() # m 테스트 케이스의 길이
    nums = list(input().split()) # 문자 입력
    n_dict = { "ZRO":0,"ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7,"EGT":8, "NIN":9}
    list_keys = list(n_dict.keys())

    area = [0,0,0,0,0,0,0,0,0,0]

    for num in nums:
        for key in n_dict.keys():
            if num == key:
                area[n_dict[key]] += 1


    # 등장횟수 만큼 배열에 추가됨
    result =''

    print("#{}".format(test_case))
    for i in range(len(area)):
        for j in range(area[i]):
            print( list_keys[i], end=' ')
        # result += ( area[i] *  list_keys[i] , end=' ')






