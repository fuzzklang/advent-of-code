import sys

def checkSlope(L, rightSteps, downSteps):
    """For part 2"""
    wrap = len(L[0])
    idx = 0
    nTrees = 0
    for line in L[downSteps::downSteps]:
        idx = (idx + rightSteps) % wrap
        if line[idx] == "#":
            nTrees += 1
    return nTrees

L = []
for line in sys.stdin:
    L.append(line.strip())

print("Part 1")
wrap = len(L[0])
idx = 0
nTrees = 0
for line in L[1:]:
    idx = (idx + 3) % wrap
    if line[idx] == "#":
        nTrees += 1

print("Number of trees:", nTrees)

a = checkSlope(L, 1, 1)
b = checkSlope(L, 3, 1)
c = checkSlope(L, 5, 1)
d = checkSlope(L, 7, 1)
e = checkSlope(L, 1, 2)
print(a, b, c, d, e)
print("Multiplied result:", a*b*c*d*e)
