# Given an integer number, find the square root of it using Binary Search technique:

def findsqrt(n):
    global mid
    low = 0
    high = n

    while low < high:
        mid = (low + high) // 2
        if mid * mid > n:
            high = high - 1
        else:
            low = low + 1
    return mid

n = int(input("Enter the number: "))
print(f"The square root of {n} is {findsqrt(n)}")
