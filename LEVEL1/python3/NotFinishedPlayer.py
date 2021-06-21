from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):  # zip으로 두 리스트를 묶어서 비교
        if p != c:                             # 두 리스트가 정렬되어있으므로 값이 다르면 해당 참가자는 완주하지 못한 것
            return p
    return participant[-1]                     # 참가자가 리스트의 맨 뒤에 있을 경우 고려

def othersolution(participant, completion):    # counter를 활용한 풀이
    '''
    collections.Counter() => 컨테이너에 동일한 값의 자료가 몇 개인지를 파악하는데 사용하는 객체
                          => 출력 결과를 Counter(Dict)형태로 반환 Counter({'leo' : 1, 'kiki' : 1, 'eden' : 1})
                          => 덧셈, 뺄셈 등의 연산 가능, 합집합, 교집합 연산도 가능

    '''
    answer = Counter(participant) - Counter(completion)

def main():
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(list(Counter(participant) - Counter(completion))[0])
    print(solution(participant, completion))

main()