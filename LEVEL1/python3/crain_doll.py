def pick(board, index, n):      # 크레인 동작 순서에 해당하는 위치에 따라 가장 상단 인형 pick
    top = -1            
    for i in range(n):
        if board[i][index]:     # 상단에서 부터 탐색 => 인형이 있으면
            top = board[i][index]   # 인형 pick
            board[i][index] = 0     # 원래 인형이 있던 자리에 인형이 없어졌으므로
            break

    return top

def in_busket(pick, busket, count):                 # pick한 인형을 가지고 처리
    if len(busket) != 0 and busket[-1] == pick:     # busket이 비어있지 않고 현재 들어올 인형과 마지막 인형이 일치하면
        del busket[-1]                              # 터짐
        count += 2                                  # 터뜨린 인형 카운트

    else :                                          # 일치하지 않으면
        if pick != 0:                               # ☆크레인이 0을 집어올 수 있으므로 배제(여기서 오류있었음!)
            busket.append(pick)                     # busket에 인형 담기

    return count                                    # 이번 차례에 터뜨린 인형 수 반환
    
def solution(board, moves):
    n = len(board)
    busket = []
    count = 0
    
    for m in moves:                 # 크레인 동작 순서
        index = m-1
        p = pick(board, index, n)   # 인형을 집는 과정
        count = in_busket(p, busket, count)     # 인형을 집어서 바구니에 놓고 터뜨리기
    
    return count

def main():
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))

main()

def othersolution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer