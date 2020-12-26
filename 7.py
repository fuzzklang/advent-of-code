import sys

bags = dict()

class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = dict()     # children
        self.contained_in = list() # parents

    def addChild(self, child, number):
        self.contains[child] = number

    def addParent(self, parent):
        self.contained_in.append(parent)

    def getAncestors(self):
        # Return set of all ancestors, using recursion
        ancestors = set(self.contained_in)
        for parent in self.contained_in:
            ancestors = ancestors.union(bags[parent].getAncestors())
        return ancestors

    def getNumAncestors(self):
        return len(self.getAncestors())

    def getNumBagsContained(self):
        # Return number of accumulated bags in all succesor-bags, recursively
        num = 0
        for child in self.contains:
            num += self.contains[child] # number of child-bags in this bag
            # Number of bags in individual child bag multiplied by the number of
            # this type in current bag.
            num += bags[child].getNumBagsContained() * self.contains[child]
        return num

    def printChildren(self):
        print(f"{self.name} bags contain:")
        for key in self.contains:
            print("", self.contains[key], key, "bag(s)")

    def printParents(self):
        print(f"{self.name} is contained in:")
        for parent in self.contained_in:
            print("", parent)

L = []
for line in sys.stdin:
    L.append(line)

for s in L:
    bag, desc = s.strip().split("bags contain")
    # i.e. -> 'dark indigo', '2 pale blue bags, 1 dark violet bag.'
    bag = bag.strip()
    bags[bag] = Bag(bag)

    desc = desc[:-1].strip() # remove full point at end
    descs = [d.strip() for d in desc.split(',')]
    # -> list of descriptions of bags contained
    for d in descs:
        if not d == "no other bags":
            # add children of current bag
            # else, no children
            n, contained_bag = d.split(" ", 1) # retrieve number
            n = int(n.strip())
            contained_bag = contained_bag.rsplit(" ", 1)[0]   # remove 'bag' from description
            bags[bag].addChild(contained_bag, n)

# Add parents of bags for all bags in dict
for bag in bags:
    for child in bags[bag].contains:
        bags[child].addParent(bag)

print("Part 1")
print(f"Total number of bags: {len(bags)}")
print(f"Number of bag colors which can contain at least one shiny gold bag: {bags['shiny gold'].getNumAncestors()}")

print("Part 2")
print(f"Total number of bags required inside a single shiny gold bag: {bags['shiny gold'].getNumBagsContained()}")
