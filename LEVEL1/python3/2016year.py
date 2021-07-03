def solution(a, b):
    DOW = {0 : 'FRI', 1 : 'SAT', 2 : 'SUN', 3 : 'MON', 4 : 'TUE', 5 : 'WED', 6 : 'THU'}   # day of weekend
    num_of_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    progressed_day = sum([num_of_day[i] for i in range(a-1)]) + b-1
    return DOW[progressed_day % 7]

# other solution
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))