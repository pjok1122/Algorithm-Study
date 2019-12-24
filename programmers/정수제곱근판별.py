def solution(n):
    if n == 1:
        return 4
    for i in range(n//2):
        if i*i == n:
            return (i+1)*(i+1)
    return -1
print(solution(3))
print(solution(121))
print(solution(144))
print(solution(1))
print(solution(2))
