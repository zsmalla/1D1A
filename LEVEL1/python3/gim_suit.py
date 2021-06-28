import time
def solution(n, lost, reserve):
    result = [1]*n          # 처음에 모두 한 벌씩 있다고 가정
    for i in range(n):
        if i+1 in lost:     # 잃어버린 학생
            result[i] -= 1
        if i+1 in reserve:  # 여벌을 가지고 있는 학생       => 여벌을 가지고 있지만 잃어버릴 경우 +-0
            result[i] += 1
            
    for i in range(n):      # 왼쪽 학생한테 빌리기
        if result[i] == 0:
            if i > 0 and result[i-1] == 2:
                result[i-1] -= 1
                result[i] += 1

        if result[i] == 0:  # 오른쪽 학생한테 빌리기
            if i < n-1 and result[i+1] == 2:
                result[i+1] -= 1
                result[i] += 1
    # return result
    return n - result.count(0)      # 한 벌도 갖고 있지 않은 학생은 수업에 참가 x


def othersolution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]        # 여분이 있고, 잃어버리지 않은 학생 list
    _lost = [l for l in lost if l not in reserve]           # 잃어버리고, 여분이 없는 학생 list
    for r in _reserve:          # 체육복이 2개인 학생들의
        f = r - 1               # 왼쪽 학생
        b = r + 1               # 오른쪽 학생        
        if f in _lost:          # 왼쪽 학생이 체육복이 없으면
            _lost.remove(f)     # 한 벌을 주고 왼쪽 학생을 lost에서 제거
        elif b in _lost:        # 왼쪽 학생은 있지만 오른쪽 학생이 체육복이 없으면
            _lost.remove(b)     # 한 벌을 주고 오른쪽 학생을 lost에서 제거
    return n - len(_lost)       # lost에 포함된 학생을 제외하고 모두 수업 참가 ㄱㄴ

'''
알아둬야할 점
in연산자는 O(n)의 시간 복잡도
코드를 간결하게 쓰도록 하자!
내 꺼 10만 번 : 0.2353963851928711
밑에 꺼 10만 번 : 0.14661383628845215
'''