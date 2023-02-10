def hist(nums):
    current = '*'
    for num in nums:
        if num != 0:
            current *= num
        else:
            current = ''
        print(current)
        current = '*'