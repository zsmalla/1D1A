def solution(numbers, hand):
    answer = ''
    LH = (3, 0)     # 초기 왼손의 위치
    RH = (3, 2)     # 초기 오른손의 위치
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]      # 키패드
    for num in numbers:
        if num in [i[0] for i in keypad] :                                                  # 왼쪽 열의 숫자들을 입력할 때는
            answer += 'L'                                                                   # 왼손 이용
            LH = [(i,j) for i in range(4) for j in range(3) if keypad[i][j] == num][0]      # 현재 왼손의 위치 업데이트
        elif num in [i[2] for i in keypad] :                                                # 오른쪽 열의 숫자들을 입력할 때는
            answer += 'R'                                                                   # 오른손 이용
            RH = [(i,j) for i in range(4) for j in range(3) if keypad[i][j] == num][0]      # 현재 오른손의 위치 업데이트
        else :                                                                              # 가운데 열의 숫자들을 입력할 때는
            idx = [(i, j) for i in range(4) for j in range(3) if keypad[i][j] == num][0]    # 입력하고자 하는 숫자의 인덱스와
            if getdist(LH, idx) > getdist(RH, idx):                                         # 현재 왼손, 오른손의 위치를 비교해서
                answer += 'R'                                                               # 거리가 더 작은 쪽의 손을 이용
                RH = idx                                                                    # 이용한 손의 위치 업데이트
            elif getdist(LH, idx) < getdist(RH, idx):
                answer += 'L'
                LH = idx
            else : 
                answer += hand[0].upper()                                                   # 입력하고자 하는 숫자와 왼쪽과 오른쪽 손의 거리가 같은 경우 
                if hand == "left" : LH = idx                                                # 사용자가 왼손잡이인 경우 왼손 이용
                else : RH = idx                                                             # 오른손 잡이인 경우 오른손 이용

    return answer

def getdist(HP, idx):
    return abs(idx[0]-HP[0]) + abs(idx[1] - HP[1])


def main():
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    print(solution(numbers, hand))

main()

'''
self-feedback
keypad 리스트를 저장하기 보다는 딕셔너리 자료형을 사용해서
keypad = {1:(0,0), 2:(0,1), ...} 이렇게 저장했으면 인덱스를 매번 구하지 않아도 되어서 더 효율적으로 코드 구성이 가능했을 것 같다.
'''