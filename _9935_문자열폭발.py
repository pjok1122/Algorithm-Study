'''

'''
import sys
input = sys.stdin.readline

s = input().strip()
boom = list(input().strip())

stack = []

# 시간 초과
# while 1:
#     if s.count(boom) > 0:
#         s = s.replace(boom, "")
#     else:
#         break
# s = s if len(s) > 0 else "FRULA"

for char in s:
    stack.append(char)

    if stack[-len(boom):] == boom:  # stack[(len(stack)-len(boom)):] == stack[-len(boom):]
        for i in range(len(boom)):
            stack.pop(-1)

print(''.join(stack) if len(stack) > 0 else "FRULA")
