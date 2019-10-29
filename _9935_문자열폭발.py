import sys
input = sys.stdin.readline

s = input()
boom = input()
boom.strip()  # not working

while 1:
    if s.count(boom) > 0:
        s = s.replace(boom, "")
    else:
        break
s = s if len(s) > 0 else "FRULA"
print(s)
