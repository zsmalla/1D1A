import re

def solution(dartResult):
    st = '[0-9]*[SDT][*#]*'                                 # 정규식을 이렇게 작성할 경우 한 문자씩 별개로 풀 수 밖에 없었음 
    m = re.findall(st,dartResult)                           # other_solution처럼 그룹핑으로 묶어서 생각했어야함
    result = []
    print(m)                                                # ['1D', '2S#', '10S']
    for str in m:
        str = str.translate(str.maketrans('SDT','123'))     # 'S', 'D', 'T'에 해당하는 문자를 각각 '1', '2', '3'으로 치환 
        if len(str) == 2 :                                  # 아니 그동안 딕셔너리 활용 잘 했으면서 왜 이렇게 했는지..?
            result.append(int(str[0])**int(str[1]))
        elif len(str) == 3:                     
            if str[1] =='0':
                result.append(int(str[0:2])**int(str[2]))
            elif str[2] == '*':
                if len(result) != 0 : result[-1] *= 2
                result.append(2*int(str[0])**int(str[1]))
            elif str[2] == '#':
                result.append(-1*int(str[0])**int(str[1]))
        elif len(str) == 4:                                  # 정규표현식에서 그룹핑을 했다면 이렇게 많은 if-else 필요 없었을 듯 싶다.
            if str[3] == '*':
                if not len(result) : result[-1] *= 2
                result.append(2*int(str[0:2])**int(str[2]))
            elif str[3] == '#':
                result.append(-1*int(str[0:2])**int(str[2]))

    return sum(result)


def other_solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')                   # 그룹핑(괄호처리) 잘 알아두자
    dart = p.findall(dartResult)
    print(dart)                                             # [('1', 'D', ''), ('2', 'S', '#'), ('10', 'S', '')]
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


