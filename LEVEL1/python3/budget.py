def solution(d, budget):
    count =0
    d.sort()
    for request in d:
        result = budget - request
        if result >= 0:
            count += 1
            budget = result
        else : return count
    return count