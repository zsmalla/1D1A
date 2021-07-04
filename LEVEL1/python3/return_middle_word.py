def solution(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s)//2-1 : len(s)//2+1]

def othersolution(s):
    return s[(len(s)-1)//2 : len(s)//2+1]       # 인덱스가 소수점이면 정수 인덱스가 적용되므로 if문은 안써도 문제 없었을듯

print(othersolution("powerr"))       