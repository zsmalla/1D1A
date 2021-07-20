def solution(numbers):
    answer = sorted(set([numbers[i] + numbers[j] for i in range(len(numbers)-1) for j in range(i+1, len(numbers))]))
    return answer


'''
이제 list comprehension의 감이 잡힌듯..?
'''