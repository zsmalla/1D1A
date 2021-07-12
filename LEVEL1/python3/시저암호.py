def solution(s, n):
    answer = ''
    for c in s:
        if c.islower():     # 문자가 소문자인 경우
            answer += chr(97+((ord(c)-97)+n)%26)
        elif c.isspace():   # 공백인 경우
            answer += ' '
        else:               # 이외의 경우 => 이 문제에서 이외의 경우는 대문자인 경우 밖에 없음
            answer += chr(65+((ord(c)-65)+n)%26)
    return answer

def othersolution(s, n):
    s = list(s)                 # 문자열 s를 리스트로 변환해서 풀이한 other solution
    for i in range(len(s)):     # 리스트로 변환하면 자동으로 공백까지 원소로 포함되어서
        if s[i].isupper():      # 이런식으로 대문자, 소문자만 고려해서 변경해주면 된다.
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)           # 리스트를 문자열로 변환할 때는 .join() 메서드 