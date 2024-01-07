import sys

n = int(sys.stdin.readline().strip())  # size of the input
arr = list(map(int, sys.stdin.readline().strip().split()))  # taking input of every element

total = (1 << n)
for i in range(1, total):
    subset = [arr[j] for j in range(n) if (i & (1 << j))]
    sys.stdout.write(" ".join(map(str, subset)) + "\n")