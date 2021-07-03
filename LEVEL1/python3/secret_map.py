from collections import deque

def T2B(n,num):         # 숫자의 2진수를 구해 지도의 크기에 맞도록 비트(0)를 추가한 리스트를 반환하는 함수
    result = deque()
    while num > 0:
        result.append(num%2)
        num //= 2
    result.reverse()
    if n-len(result) > 0:
        for _ in range(n-len(result)) : result.appendleft(0)
    return list(result)
    
def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        tmp1 = T2B(n,a)
        tmp2 = T2B(n,b)
        tmp = ''
        for t1, t2 in zip(tmp1, tmp2):
            tmp += ' ' if t1==t2==0 else '#'
        answer.append(tmp)
    return answer

def main():
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(other_solution(n, arr1, arr2))
    

main()

def other_solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = bin(i|j)[2:]          # 1. 비트 or 연산, 2. 2진수 문자열로 변환(bin())
        a12=a12.rjust(n,'0')        # 문자열의 크기가 n이 될 때까지 '0'bit을 추가
        a12=a12.replace('1','#')    # '1'을 '#'으로 변환
        a12=a12.replace('0',' ')    # '0'을 ' '으로 변환
        answer.append(a12)
    return answer




