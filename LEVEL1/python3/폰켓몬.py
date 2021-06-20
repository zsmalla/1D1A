def solution(nums):
    n = len(nums)
    N = n / 2
    a = set()
    for num in nums:
        a.add(num)
    if len(a) < N:
        answer = len(a)
    else:
        answer = int(N)

    return answer

def main():
    nums = [3,3,3,2,2,4]
    print(solution(nums))

main()