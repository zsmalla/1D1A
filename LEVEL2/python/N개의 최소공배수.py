def solution(arr):
    m = max(arr)
    mul = 1
    while True:
        count = 0
        for i in arr:
            if (m * mul)%i == 0 : count += 1
        if count == len(arr) : return m*mul
        else : mul += 1