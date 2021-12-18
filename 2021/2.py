import sys

# Read in data
L = []
for line in sys.stdin:
    L.append(line)

print("PART 1")
hor_pos = 0
depth = 0

for line in L:
    cmd, val = line.split()
    val = int(val)
    if cmd == "forward":
        hor_pos += val
    elif cmd == "down":
        depth += val
    elif cmd == "up":
        depth -= val

print(hor_pos * depth)


print("PART 2")
hor_pos = 0
depth = 0
aim = 0

for line in L:
    cmd, val = line.split()
    val = int(val)
    if cmd == "forward":
        hor_pos += val
        depth += aim * val
    elif cmd == "down":
        aim += val
    elif cmd == "up":
        aim -= val

print(hor_pos * depth)
