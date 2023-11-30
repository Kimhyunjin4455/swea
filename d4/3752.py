T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    visited = [1] + [0] * sum(arr)
    nums = [0]

    for i in arr:
        for j in range(len(nums)):
            # i==2 -> nums {0,2}
            # i==3 -> nums {0,2,3,5}
            # i==5 -> nums {0,2,3,5,7,8,10}
            if visited[i + nums[j]] == 0:
                visited[i+nums[j]] = 1
                nums.append(i+nums[j])


    print("#{} {}".format(tc, len(nums)))
