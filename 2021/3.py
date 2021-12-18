import sys

# Read in data
L = []
for line in sys.stdin:
    L.append(line)

print("PART 1")

ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma_bits = list(range(12))

for line in L:
    for idx, bit in enumerate(line):
        if bit == "1":
            ones[idx] += 1

for idx, bit in enumerate(gamma_bits):
    if ones[idx] > len(L)/2:
        gamma_bits[idx] = 1
    else:
        gamma_bits[idx] = 0

gamma_bitstring = "".join([str(bit) for bit in gamma_bits])
epsilon_bitstring = "".join(["1" if bit == "0" else "0" for bit in gamma_bitstring])

gamma_rate = int(gamma_bitstring, base=2)
epsilon_rate = int(epsilon_bitstring, base=2)

print(gamma_rate * epsilon_rate)


print("PART 2")
# 1. Finn bit_criteria (enten Most Common eller Least Common for hver kolonne.)
# 2. Filtrer ut strenger basert på bit-kriteriet ("0" eller "1").
# 3. Fortsett rekursivt med den filtrerte listen og på neste bit-posisjon

def find_bit_criteria(lst, pos, mode):
    """Mode: if bit-criteria is determined by most common or least common value.
    Also determines what to return in case of equal amounts of zeros and ones.
    '1': oxygen generator rating (most common value)
    '0': co2 scrubber rating (least common value)
    """
    zeros = 0
    ones = 0
    for bitstring in lst:
        if bitstring[pos] == "0":
            zeros += 1
        elif bitstring[pos] == "1":
            ones += 1
    if zeros > ones:
        most_common = "0"
        least_common = "1"
    elif zeros < ones:
        most_common = "1"
        least_common = "0"
    elif zeros == ones:
        return mode  # "0" or "1" depending on mode
    if mode == "1":
        return most_common
    elif mode == "0":
        return least_common


def filter_rec(lst, pos, mode):
    """mode: '0' or '1'"""
    if len(lst) == 1:
        return lst[0]
    filtered_list = []
    bit_criteria = find_bit_criteria(lst, pos, mode)
    for bitstring in lst:
        if bitstring[pos] == bit_criteria:
            filtered_list.append(bitstring)
    return filter_rec(filtered_list, pos+1, mode)

oxygen_gen_rating = int(filter_rec(L, 0, "1"), base=2)
co2_scrubber_rating = int(filter_rec(L, 0, "0"), base=2)
print(oxygen_gen_rating * co2_scrubber_rating)
