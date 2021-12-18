import sys

# Read in data
L = []
for line in sys.stdin:
    L.append(int(line))

print("PART 1")
count = 0
current = L[0]
for measurement in L[1:]:
    if measurement > current:
        count += 1
    current = measurement

print(count)
print()

print("PART 2")
count = 0
current = L[0] + L[1] + L[2]
for idx in range(1, len(L[1:-1])):
    next_sum = L[idx] + L[idx + 1] + L[idx + 2]
    if next_sum > current:
        count += 1
    current = next_sum

print(count)
