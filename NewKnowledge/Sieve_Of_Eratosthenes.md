# 에라토스테네스의 체(Sieve Of Eratosthenes)
소수를 판별하는 알고리즘 중 하나, 특정 범위의 많은 소수들을 구할 때 가장 유용한 알고리즘(현존하는 것 중에 가장 빠르다고 함)

## 알고리즘
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열
2. 2부터 시작, 가장 작은 2를 소수로 선택하고 2의 배수를 지우기
3. 3도 소수로 선택, 3의 배수 지우기
4. 4는 2의 배수이므로 지워졌고, 5로 넘어감
5. 2~4 과정 반복 <br>
5-1. 이때 n의 배수를 지우는 과정에서 n의 범위는 sqrt(n)까지 검사 : n의 최대 약수가 sqrt(n)이하이기 때문 <br>
5-2. 이미 소수가 아니라고 판정된 수도 건너 뜀 : 효율성 up
6. 남아있는 수가 소수

![과정](https://commons.wikimedia.org/wiki/File:Sieve_of_Eratosthenes_animation.gif)


```python
def solution(n):               
    table = [True] * (n+1)                           # 과정 1 (table의 인덱스는 0 ~ n)
    sqrt_n = int(n**0.5)                             # 과정 5-1
    for i in range(2, sqrt_n+1):                     # 과정 5
        if table[i]:                                 # 과정 5-2
            for j in range(i*2, n+1, i):             # 과정 2~4
                table[j] = False
    result = [i for i in range(2, n+1) if table[i]]  # 과정 6
```