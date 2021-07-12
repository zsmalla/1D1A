def solution(s):
    s = list(s)
    answer = ''
    j = 0       # 다른 word가 나올 때 마다 인덱스 초기화(공백으로 구분) 
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            j = 0
        else:
            answer += s[i].upper() if j % 2 == 0 else s[i].lower()
            j += 1

    return answer

def othersolution(s):       # list comprehension을 이용한 othersolution
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))