import sys

L = []
for line in sys.stdin:
    L.append(line)

# --- Part 1 ---
acc = 0
group = ""
for l in L:
    l = l.strip()
    if l:
        group += l
    else:
        acc += len(set(group))
        group = ""
else:
    # Add last line in case no ending newline
    acc += len(set(group))

print("Part 1")
print(f"Sum of questions answered is {acc}")

# --- Part 2 ---
# Group in list of lists
groups = []
g = []
for l in L:
    l = l.strip()
    if l:
        g.append(l)
    else:
        groups.append(g)
        g = []
else:
    # Add last line
    if l:
        g.append(l)
        groups.append(g)

# Take union of sets and count members
acc = 0
for g in groups:
    accIntersect = set(g[0])
    for entry in g[1:]:
        accIntersect = accIntersect.intersection(set(entry))
    acc += len(accIntersect)

print("Part 2")
print(f"Sum of questions answered is {acc}")
