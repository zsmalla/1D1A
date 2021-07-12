def solution(n):                # n = 20
    table = [True] * (n+1)      # 0 ~ 21
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n+1):          # index : 0 ~ 19
        for j in range(i*2, n+1, i):
            table[j] = False

    result = [i for i in range(n+1) if i > 1 and table[i]]
    return len(result)
    # return len([i for i in range(1,n+1) if len([a for a in range(1,i+1) if i%a ==0]) == 2]) #시간 초과
solution(10)

''' 알아둬야 할 것
에라토스테네스의 체 : 현존하는 n까지의 소수 구하는 방법 중 가장 빠른 방법
'''

def solution(n):               # 조금 더 다듬은 버전 
    table = [True] * (n+1)      
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n+1):          
        if table[i]:
            for j in range(i*2, n+1, i):
                table[j] = False
    result = [i for i in range(2, n+1) if table[i]]
