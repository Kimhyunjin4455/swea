T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    coin_list = [50000,10000,5000,1000,500,100,50,10]
    change_list = [0,0,0,0,0,0,0,0]
    result = ""
    for i in range(len(coin_list)):
        if n >= coin_list[i]:
            change_list[i] += (n // coin_list[i] )
            n -= (coin_list[i] * (n // coin_list[i]))
    for change in change_list:
        result += (str(change)+" ")
    print("#{}".format(test_case))
    print(result)
