import sys

L = []
for line in sys.stdin:
    L.append(line)

def findSeat(s):
    row = 0
    adder = 64
    for l in s[:7]:
        if l == "B":
            row += adder
        adder //= 2
    col = 0
    adder = 4
    for l in s[7:]:
        if l == "R":
            col += adder
        adder //= 2
    return (row, col)

def calcSeatID(seating):
    row, col = seating
    return row * 8 + col

def highestSeatID(L):
    highest = 0
    for s in L:
        val = calcSeatID(findSeat(s))
        if val > highest:
            highest = val
    return highest

def makeOverview(L):
    overview = [[0]*8 for i in range(128)]
    for seating in L:
        row, col = findSeat(seating)
        overview[row - 1][col - 1] = 1
    return overview

def printOverview(seatingOverview):
    for no, row in enumerate(seatingOverview):
        r = ''.join('X' if c else '.' for c in row)
        print("{:3}:".format(no + 1), r)

def findMySeat(overview):
    for i, row in enumerate(overview[1:-1]):
        for j, col in enumerate(overview[i]):
            if overview[i - 1][j] and overview[i + 1][j] and not overview[i][j]:
                return (i + 1, j + 1)


print("Part 1")
print(f"Highest seat ID: {highestSeatID(L)}")

print("Part 2")
#printOverview(makeOverview(L))
mySeat = findMySeat(makeOverview(L))
print(f"My seat: {mySeat}, seatID: {calcSeatID(mySeat)}")
