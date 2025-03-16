def sortedSquares(nums):
    parr = []
    narr = []
    rarr = []

    for i in nums:
        if i < 0:
            narr.append(i ** 2)
        else:
            parr.append(i ** 2)

    lenofnarr = len(narr)
    lenofparr = len(parr)

    i = 0
    j = lenofnarr - 1
    k = 0
    while j >= 0 and i < lenofparr:
        if parr[i] < narr[j]:
            rarr.append(parr[i])
            i += 1
        elif parr[i] > narr[j]:
            rarr.append(narr[j])
            j -= 1
        else:
            rarr.append(parr[i])
            rarr.append(narr[j])
            i += 1
            j -= 1
    while j >= 0:
        rarr.append(narr[j])
        j -= 1

    while i <= lenofparr - 1:
        rarr.append(parr[i])
        i += 1

    return rarr

    print(rarr)




nums = [-7,-3,2,3,11]
sortedSquares(nums)