def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if answers[i] == one[i%5] : result[1] += 1
        if answers[i] == two[i%8] : result[2] += 1
        if answers[i] == thr[i%10] : result[3] += 1
    return [key for key, value in result.items() if value == max(result.values())]

print(solution([1,3,2,4,2]))

'''
알아둬야 할 점
dictionary 자료형에서 value로 key 찾기(dict.items())
                     values만 따로 반환(dict.values())
'''

def othersolution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

'''
enumerate로 인덱싱까지 한 번에 하는 방법도 있음 근데 dict써서 하는게 더 빠른 결과가 나왔음
'''