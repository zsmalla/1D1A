def solution(new_id):
    rm_char = ['-', '_', '.']
    
    new_id = new_id.lower()                             # 1단계 : 모든 문자를 소문자로 치환

    for c in new_id:
        if not c.isalnum() and c not in rm_char:
            new_id = new_id.replace(c, "")              # 2단계 : 숫자+소문자, 특정 기호를 제외한 모든 기호 제거
            
    while '..' in new_id:
        new_id = new_id.replace('..', '.')              # 3단계 : 연속된 마침표 치환

    while new_id[0] == '.' or new_id[-1] == '.':        # 4단계 : 첫 번째와 마지막 문자 마침표인 경우 제거
        new_id = new_id.strip('.')  
        if new_id == '' :                               # 5단계 : 공백인 경우 'a'로 채우기
            new_id = "aaa"
            break
    
    if len(new_id) >= 15 :                              # 6단계 : 16자 이상인 경우 15자리까지 + 마지막 마침표 제거
        new_id = new_id[:15].rstrip('.') 

    while len(new_id) <= 2:                             # 7단계 : 2자 이하인 경우 마지막 문자로 채움                    
        new_id += new_id[-1]
    
    return new_id

'''
생각했어야 할 부분
1. 문자열 메소드 사용시 new_id.replace() 이케만 쓰면 그냥 반환만 됌 => new_id = new_id.replace() 이렇게 대입으로
=> 이거때문에 계속 무한루프
2. 문자열은 요소 임의 조작 불가능 => 제거해야 할 경우 replace() 메소드 사용하거나 다른 문자열로 옮겨야함
3. 양쪽 끝 특정 문자를 제거해야할 경우 strip() 사용
'''





