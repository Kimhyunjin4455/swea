T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    s_nums = sorted(nums)
    s_nums.remove(s_nums[0])
    s_nums.remove(s_nums[-1])

    res = sum(s_nums) / len(s_nums)

    print("#{} {}".format(tc, round(res)))