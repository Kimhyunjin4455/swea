T = int(input())

# 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
# 2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
# 3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
# 4. 각각의 십진수를 아스키 코드로 변환한다.
# <Encoding> 8bit 3글자 -> 6bit 4글자
# <Decoding> 6bit 4글자 -> 8bit 3글자

# 표 1
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]

for test_case in range(1,T+1):
    character = list(map(str, list(input())))
    res = ''

    for i in range(len(character)):
        num = decode.index(character[i])

        bin_num = str(bin(num)[2:]) # 이진수로 변환

        # bin_num의 길이가 6보다 작으면 앞에 0 붙여주기
        # 1을 이진수로 바꾸면 1로 나옴(필요한 값은 000001임)
        while len(bin_num)<6:
            bin_num = '0'+bin_num

        res += bin_num # 변환한 값을 하나의 값(str)으로

    result = ''

    for j in range(len(character) * 6 // 8): # 만들어진 값(글자의 길이 * 6)을 8비트 단위로 자름
        # 자른 값을 10진수로 변환
        e = int(res[j * 8:j * 8 + 8], 2) # 8비트로 자른 값을 10진수로 변환
        result += chr(e)

    print("#{} {}".format(test_case, result))





