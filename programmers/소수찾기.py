'''
prime number = 1과 자기 자신을 약수로 갖는 수 
'''
def solution(n):
    answer = []
    for i in range(2,n+1,1):
        prime=i
        for j in range(2, i//2+1, 1):  
            if i%j==0:
                prime=0
                break
        if prime != 0:        
            answer.append(prime)
    return len(answer)
print(solution(10))