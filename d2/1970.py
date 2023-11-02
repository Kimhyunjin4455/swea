T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    coin_list = [50000,10000,5000,1000,500,100,50,10]
    change = [0,0,0,0,0,0,0,0]
    for coin in range(len(coin_list)):
        if n > coin_list[coin]:
            n -= (coin * (n // coin))
            change[coin] += 1
    print("")
