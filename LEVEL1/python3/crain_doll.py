def set_state(state, board, n):
    state = [0]*n
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 :
                state[i] += 1
                

def solution(board, moves):
    N = len(board)
    n = len(moves)
    state = [0]*N
    result = 0
    
    for i in range(n):
        current = board[state[moves[i]]][i]
        next = board[state[moves[i]]][i]
        if current == next:
            result += 1
            next = -1
        board[state[moves[i]]][i] = 0
    set_state(state, board, N)
        
    return result

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))