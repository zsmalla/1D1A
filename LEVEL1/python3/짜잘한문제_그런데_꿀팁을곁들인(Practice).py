''' 짜잘한 연습문제 모아놓기'''

''' 같은 숫자는 싫어
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
'''
def solution(arr):
    answer = [arr[0]]                   # 첫 번째 원소는 넣어놓고
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:        # result 리스트의 마지막 원소와 들어올 원소가 같으면 연속이므로 배제
            answer.append(arr[i])

    return answer       # 굳

''' 나누어 떨어지는 숫자 배열
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
'''
def solution(arr, divisor):
    result = [a for a in arr if a % divisor == 0]
    return sorted(result) if len(result) != 0 else [-1]

def othersolution(arr, divisor):
    return sorted([a for a in arr if a % divisor == 0]) or [-1]     # or 연산자의 경우 앞이 거짓이면 뒤의 값이 호출되므로
                                                                    # 리스트에 값이 없으면 거짓으로 판단, return[-1] 호출

''' 두 정수 사이의 합
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다. a와 b의 대소관계는 정해져있지 않습니다.
'''
def solution(a, b): return sum(list(range(a,b+1)))if a<=b else sum(list(range(b,a+1)))  # range()객체를 list로 변환 안시켜도 sum 적용 됨!

''' 문자열 내 마음대로 정리하기
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
'''
def solution(strings, n):
    return sorted(strings, key=lambda s : (s[n],s)) # 정렬 기준 1 : n번째 인덱스 문자, 기준 2 : 사전순서    굳!

''' 문자열 내 p와 y의 개수
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
'''
def solution(s):
    return True if s.lower().count('p') == s.lower().count('y') else False  # 이제 좀 뭔가 된다..?

''' 문자열 내림차순으로 배치하기
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
'''
def solution(s):
    answer = ''
    s = sorted(s, key = lambda x : -ord(x))     # 아스키 코드는 대문자 abc... -> 소문자 abc.. 순으로 가므로 역순으로 정렬
    for i in s:                                 # sorted를 사용하면 문자열도 리스트로 변환 후 정렬할 수 있다.
        answer += i
    return answer

def othersolution(s):
    return ''.join(sorted(s, reverse=True))     # list의 각 문자들을 하나의 문자열로 묶으려면 join()을 사용하면 되었다.

''' 문자열 다루기 기본
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
'''
def solution(s):
    return (len(s)==2 or len(s)==4) and s.isdigit() # and 앞의 조건을 len(s) in (2, 4)로 했으면 좀 더 깔끔했을 것 같다.
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))     # 정규표현식을 활용한 예 {}안의 숫자는 몇 번 반복되었는지

''' 서울에서 김서방 찾기
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
'''
def solution(seoul):
    return "김서방은 %d에 있다" % seoul.index('Kim')    # 굳

''' 수박수박수박수
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
'''
def solution(n):
    sample = '수박'
    answer = ''
    for i in range(n):
        answer += sample[i%2]
    return answer

def other_solution(n):
    return "".join(["수박"[i%2] for i in range(n)])     # 리스트에 있는 항목을 문자열에 더할 때 join 까먹음 


''' 약수의 합
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''
def solution(n):
    l = [i for i in range(1, n+1) if n%i==0]
    return sum(l)

def othersolution(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

''' 자릿수 더하기
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
'''
def solution(n):
    return sum(map(int, str(n)))

''' 자연수 뒤집어 배열로 만들기
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
'''
def solution(n):
    lst = [i for i in map(int, str(n))]
  # lst = [i for i in map(int, reversed(str(n)))]       # reversed() 메소드를 이용한 reverse
  # lst.reverse()                                       # reverse() 메소드를 이용한 reverse
    return lst[::-1]                                    # 리스트 슬라이싱을 이용한 reverse

''' 정수 내림차순으로 배치하기
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
'''
def solution(n):
    return int("".join(map(str,sorted([i for i in map(int, str(n))], key = lambda x : -x))))
    # 1. n의 각 자리 숫자를 문자로 바꾼 리스트로 변환
    # 2. 변환된 리스트를 내림차순으로 정렬
    # 3. 그걸 다시 문자로 바꿈 
    # 4. 리스트 이어붙이기
    # 5. 정수로 변환

''' 정수 제곱근 판별
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
'''
def solution(n):
    return (n**0.5+1)**2 if n**0.5 == int(n**0.5) else -1