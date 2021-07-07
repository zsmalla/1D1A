def solution(record):
    data = {}
    answer = []
    stack = []
    for str in record:
        tmp = str.split(" ")
        if tmp[0] == 'Enter':
            data[tmp[1]] = tmp[2]
            stack.append((tmp[1], tmp[0]))
        elif tmp[0] == 'Leave':
            stack.append((tmp[1], tmp[0]))
        else:
            data[tmp[1]] = tmp[2]
    for s in stack:
        if s[1] == 'Enter':
            answer.append(data[s[0]]+"님이 들어왔습니다.")
        elif s[1] == 'Leave':
            answer.append(data[s[0]]+"님이 나갔습니다.")
    print(answer)

def main():
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    solution(record)
