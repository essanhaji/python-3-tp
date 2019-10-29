# recursive call function

def double(n):
    if n == 0:
        return 0
    return double(n - 1) + 2

def vowelsCounter(s, i = 0):
    if i == len(s):
        return 0
    c = s[i]
    if c in "aeiouy":
        return vowelsCounter(s, i + 1) +1
    return  vowelsCounter(s, i + 1) +0

def fin(n):
    if n == 0 or n == 1:
        return 1
    return fin(n - 1) + fin(n - 2)

print(fin(4))
print(vowelsCounter("hello world"))
print(double(65))
