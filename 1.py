import sys

L = []
for line in sys.stdin:
    L.append(int(line.strip()))

print("Deloppgave 1")
for idx, i in enumerate(L):
    for j in L[idx:]:
        if j + i == 2020:
            print(i * j)

print("Deloppgave 2")
for idx1, i in enumerate(L):
    for idx2, j in enumerate(L[idx1:]):
        for k in L[idx2:]:
            if j + i + k == 2020:
                print(i * j * k)
