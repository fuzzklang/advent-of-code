import sys
import re

L = []
for line in sys.stdin:
    L.append(line)

class PassportCollection:
    def __init__(self):
        self.passports = list()

    def addPassport(self, string):
        passport = dict()
        fields = string.split()
        for field in fields:
            key = field.split(":")[0]
            val = field.split(":")[1]
            passport[key] = val
        self.passports.append(passport)

    def readRawInput(self, L):
        currentString = ""
        for line in L:
            if line.strip(): # not blank
                currentString += line.strip() + " "
            else:
                self.addPassport(currentString)
                currentString = ""
        if currentString: # If last line not empty
            self.addPassport(currentString)

    def valid1(self, passport):
        """For part 1"""
        reqFields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        passportFields = set(passport.keys()).difference({'cid'})
        if reqFields == passportFields:
            return True

    def valid2(self, passport):
        """For part 2"""
        p = passport
        # 'hcl': en '#' etterfulgt av 6 sifre
        # 'ecl': øyefarge én av forkortelsene i string
        # 'pid': 9 sifre, med evt. ledende 0-er
        if self.valid1(p) \
           and len(p['byr']) == 4 and '1920' <= p['byr'] <= '2002' \
           and len(p['iyr']) == 4 and '2010' <= p['iyr'] <= '2020' \
           and len(p['eyr']) == 4 and '2020' <= p['eyr'] <= '2030' \
           and self.validHgt(p['hgt']) \
           and re.match(r'^#([0-9a-f]{6})$', p['hcl']) \
           and p['ecl'] in 'amb blu brn gry grn hzl oth'\
           and re.search(r'^(\d){9}$', p['pid']):
            return True
        else:
            return False

    def validHgt(self, s):
        """Check if height is valid. Input: string, in or cm."""
        if not re.match(r'(\d+)cm$|(\d+)in$', s):
            return False  # Wrong format
        match = re.search(r'(?P<hgt>\d+)(?P<fmt>cm|in)', s)
        if match['fmt'] == 'cm':
            return '150' <= match['hgt'] <= '193'
        if match['fmt'] == 'in':
            return '59' <= match['hgt'] <= '76'

    def countValidPassports1(self):
        validPassports = 0
        for p in self.passports:
            if self.valid1(p):
                validPassports += 1
        return validPassports

    def countValidPassports2(self):
        validPassports = 0
        for p in self.passports:
            if self.valid2(p):
                validPassports += 1
        return validPassports

    def printPassports(self):
        for p in self.passports:
            print(p)

    def printValidPassports(self):
        for p in self.passports:
            if self.valid2(p):
                print(f"len: {len(p)}, passport: {p}")

p = PassportCollection()
p.readRawInput(L)
print(f"Valid passports part 1: {p.countValidPassports1()}")
print(f"Valid passports part 2: {p.countValidPassports2()}")
