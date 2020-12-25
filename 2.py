import sys

L = []
for line in sys.stdin:
    L.append(line.strip())

print("Deloppgave 1")
validPasswords = 0
for line in L:
    policy, password = line.split(":")
    char = policy[-1]
    freqs = policy.split()[0].split("-")
    freqLow = int(freqs[0])
    freqHigh = int(freqs[1])
    if freqLow <= password.count(char) <= freqHigh:
        validPasswords += 1

print("Antall gyldige passord:", validPasswords)


print("Deloppgave 2")
validPasswords = 0

for line in L:
    policy = line.split(":")[0]
    password = line.split(":")[1].strip()
    char = policy[-1]
    stringPos = policy.split()[0].split("-")
    idx1 = int(stringPos[0]) - 1
    idx2 = int(stringPos[1]) - 1
    pswdChar1 = password[idx1]
    pswdChar2 = password[idx2]
    if (pswdChar1 == char or pswdChar2 == char) and not (pswdChar1 == char and pswdChar2 == char):
        validPasswords += 1

print("Antall gyldige passord:", validPasswords)
