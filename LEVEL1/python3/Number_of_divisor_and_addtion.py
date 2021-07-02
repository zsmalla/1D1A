def solution(left, right):
    answer = 0

    for num in range(left,right+1):
        count = 0
        for i in range(1,num+1):
            if num % i ==0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer

def othersolution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

''' 
알아둬야 할 점
제곱수는 약수의 개수가 홀수, 제곱수가 아니면 짝수 
'''