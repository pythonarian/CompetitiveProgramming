def minStartValue(nums):
    l = []
    s = 0
    m = max(nums)
    hasLessThanOne = False

    while True:
        s = m
        l.clear()
        for i in nums:
            s = s + i
            l.append(s)

            if s <= 0:
                hasLessThanOne = True
                m = m + 1
                break
            # else:
            #     m = m + 1

        if hasLessThanOne == False:
            break
    return m


nums = [-3, 2, -3, 4, 2]
res = minStartValue(nums)
print(f"The Result is : {res}")