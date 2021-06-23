import itertools
def isprime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0 : count += 1

    if count > 2 : return False
    else : return True
    

def solution(nums):
    count = 0
    lst = list(map(lambda x : sum(x), itertools.combinations(nums, 3)))
#    lst = [sum(c) for c in itertools.combinations(nums,3)] # <- 이게 더 나았을 듯
    for n in lst:
        if isprime(n) : count += 1
    return count

print(solution([1, 2, 3, 4]))

"""
알아둬야 할 것
itertools 라이브러리 : 원소들의 순열과 조합을 통해 다양한 경우의 수를 추출
itertools.permutations : 순열
itertools.combinations : 조합
"""


from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def otersolution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])