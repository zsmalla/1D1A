def solution(operations):
    answer = []
    for operation in operations:
        operation = operation.split(' ')
        if operation[0] == 'I' : answer.append(int(operation[1]))
        elif operation[0] == 'D' :
            if len(answer) == 0 : continue
            else:
                answer.remove(max(answer)) if operation[1] == '1' else answer.remove(min(answer))

    return [0, 0] if len(answer) == 0 else [max(answer), min(answer)]

def main():
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))

main()
