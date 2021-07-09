def solution(s):
    num_dict = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
                'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for str in num_dict.keys():
        s = s.replace(str,num_dict[str])        # replace는 변환된 객체가 반환되는 것을 기억하자...... 멍청아...
    return int(s)

    # while s:
    #     if s[0] in num_dict.values():
    #         if len(s) == 1:
    #             answer += s
    #             break
    #         else:
    #             answer += s[0]
    #             s = s[1:]
    #     for str in num_dict.keys():
    #         if s.startswith(str):
    #            answer += num_dict[str]
    #            s = s[len(str):] 

    # return int(answer)                        # s.replace()만 썼던 자의 최후..

def main():
    s = "one4seveneight"
    print(solution(s))

main()