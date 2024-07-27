def sorting(nums: list[int]):
    freqy = [0 for i in range(201)]
    for i in nums:
        freqy[i+100] += 1
    nums.sort(key=lambda x: (freqy[x+100], -x))
    return nums

print(sorting([-1,1,-6,4,5,-6,1,4,1]))