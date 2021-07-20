def solution(jobs):
    clear, t, answer = 0, 0, 0
    arrived = []
    while not clear == len(jobs):
        for i in range(clear, len(jobs)):
            if jobs[i][0] <= t:
                arrived.append(jobs[i])
                clear += 1
        arrived.sort(key = lambda x : -x[1])
        while arrived:
            job = arrived.pop()
            answer += (t-job[0]+job[1])
            t += job[1]

    return answer//len(jobs)
    


             


    
    

def main():
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))

main()