arr = [0] * 20
subset = [0] * 20
index = 0
n = 0

def f(pos):
    global index
    if pos >= n:
        for i in range(index):
            print(subset[i], end=" ")
        print()
        return

    subset[index] = arr[pos]
    index += 1
    f(pos + 1)

    index -= 1
    f(pos + 1)


# Example usage:
arr = [1, 2, 3, 4]
n = len(arr)
f(0)