def dfs(computers, visit, next):
    if not visit[next]:
        visit[next] = True
        for i in range(len(computers)):
            if computers[next][i]:
                dfs(computers, visit, i)

def solution(n, computers):
    visit = [False]*n
    count = 0
    for i in range(n):
        if visit[i] : continue
        dfs(computers, visit, i)    
        count += 1

    return count

def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))

main()