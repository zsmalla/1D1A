def solution(n):
    com = 0
    answer = 0
    while(3**com <= n):
        com += 1
    lst = [i for i in range(com)]
    lst.reverse()
    thr = []
    for i in lst[:com]:
        thr.append(n // 3**i) 
        n = n%3**i
        if n == 0 : break
    for i, t in enumerate(thr):
        answer += t * 3**i

    return answer

print(solution(45))

def othersolution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

'''
self-feedback
진법 변환을 왜 저딴식으로 했는지..? => 나머지 연산의 결과를 이어붙인다는 생각을 안함 <-멍청함

내장함수 int()를 활용하면 10진수 -> n진수 변환이 자유롭다!!
활용 : int('11', 2) # 3
'''