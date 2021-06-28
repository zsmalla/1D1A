def solution(lottos, win_nums):
    count, zero = 0, 0
    for i in range(6):
        if lottos[i] in win_nums : count += 1
        if lottos[i] == 0 : zero += 1        
    result = 6 if count <= 1 else 7-count
    
    return [1 if result-zero <= 0 else result-zero, result]

def othersolution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

def othersolution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

'''
알아둬야 할 점
이미 지정되어 있는 값(랭크)는 사전에 정의해주어 참조할 수 있도록 하면
더 깔끔하게 완성할 수 있음
'''