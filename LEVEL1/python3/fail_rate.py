from collections import Counter

def solution(N, stage):
    n = len(stage)                                      # 총 스테이지의 개수(실패율 계산의 가변 변수로 중요!!)
    c = Counter(stage)                                  # 각 스테이지를 진행하고 있는 사람의 수 파악    => list.count(i)로도 활용 가능 근데 이건 for문 사용해서 인덱스로 접근 (O(n))
    st = {i: j for i, j in zip(c.keys(), c.values())}   # 카운터 객체를 dict형태로 변환                => counter.most_common() 메소드로 가능
    stage_range = [i+1 for i in range(N)]               # 밑에서 for i in range(1, N+1)하면 생략 가능
                               
    for i in stage_range:
        if not i in st.keys():                           # 진행하고 있는 사람이 없는 스테이지의 경우
            st[i] = 0                                    # 데이터 추가   
        if n == 0 :                                      # ZeroDivisionError 방지
            st[i] = 0
        else:                                            # 실패율을 구해서 value 교체
            tmp = st[i]                                  
            st[i] = (st[i]/n)                            # 규칙에 따라 실패율 구하는 과정
            n -= tmp                                     # st[i](스테이지 진행 사람 수)를 tmp에 따로 저장하여 활용했는데, 그냥 list를 하나 더 만들어서 사용하는게 좋았을 듯
    if N+1 in st.keys() : del st[N+1]                    # 모두 클리어 한 사람 => 에러율 구하는 과정에 사용되지 않고, 결과에도 포함되면 안되어서 삭제
    result = sorted([(i, j) for i, j in zip(st.keys(), st.values())], key=lambda s : (s[1], -s[0]), reverse = True)    # 1차로 실패율을 기준으로 내림차순 정렬
                                                                                                                       # 2차로 실패율이 같을 경우 스테이지 오름차순으로 정렬
                                                                                                                       # lambda를 활용한 다중 기준 정렬 형태 기억!!
    return [i for i, j in result]                        # 실패율이 높은 스테이지 부터 저장된 리스트 반환

def main():
    N = 5
    stage = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stage))

main()

def othersolution(N, stages):               # 동일한 접근 방법이었지만 훨씬 간결한 코드, 코드를 간결하게 작성할 수 있는 방향으로 생각을 해야될 것 같다.
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

