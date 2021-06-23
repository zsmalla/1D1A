def solution(array, commands):

    return [sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands]

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

"""
알아둬야 할 것
array.sort() : 본체의 리스트를 정렬해서 변환하는 것
sorted(array) : 정렬한 새로운 리스트를 반환 => 리스트 말고도 iterable한 자료구조 가능
"""

def othersolution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

"""
map(함수, 데이터) : 모든 데이터를 함수에 맞춰서 변환하여 반환
=>
list(map(lambda x : x*x, [1, 2, 3, 4, 5])) # 1 ~ 5까지 수를 제곱해서 리스트의 형태로 반환
"""