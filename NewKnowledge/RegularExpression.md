# 정규표현식 (RegularExpression)
정규표현식은 복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다. -> 간단히 정규식이라고도 말함

## 메타문자
-----------------------
원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다 <br>
<center> . ^ $ * + ? { } [ ] \ | ( ) </center> <br>


## 문자클래스 [ ]
-----------------------
정규 표현식이 [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"를 뜻한다. <br>

- "a"는 정규식과 일치하는 문자인 'a'가 있으므로 매치
- "before"는 'b'가 있으므로 매치
- "die"는 정규식과 일치하는 문자가 1도 없으므로 매치되지 않음 <br>

[ ] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미함 <br>
문자 클래스 안에는 어떤 문자나 메타 문자를 사용할 수 있지만 ^ 메타 문자를 사용할 경우 반대의 의미를 가짐(주의!)

- [a-zA-z] : 알파벳 모두
- [0-9] : 숫자
- [^0-9] : 숫자가 아닌 문자만 매치             
- [a-c] : [abc] : "abc"와 매치

### 자주 사용되는 문자 클래스
> \d : 숫자와 매치, [0-9] <br>
\D : 숫자를 제외한 것과 매치 [^0-9] <br>
\s : whitespace 문자와 매치 [ \t\n\r\f\v] <br>
\S : whitespace 문자를 제외한 것과 매치 [^ \t\n\r\f\v] <br>
\w : 문자 + 숫자와 매치 [a-zA-Z0-9_] <br>
>\W : 문자 + 숫자를 제외한 것과 매치 [^a-zA-Z0-9_]

## Dot(.)
------------------
줄바꿈 문자인 \n을 제외한 모든 문자와 매치 <br>
문자 클래스 내의 [.]는 문자 그대로의 ' . '를 의미(주의!) <br>
ex) a.b
- "abb"와 매치
- "aOb"와 매치
- "abb" a와 b 사이의 어떤 문자라도 하나는 있어야함 매치x

ex) a[.]b
- "a.b"와 매치
- "aOb"와 매치 x

## 반복
--------------
### 반복(*)
메타문자 * 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다는 의미 <br>
ex) ca*t
- "ct" : a가 0번 반복되어 매치
- "cat" : a가 1번 반복되어 매치
- "caaat" : a가 3번 반복되어 매치

### 반복(+)
메타문자 + 바로 앞에 있는 문자가 1부터 무한대로 반복될 수 있다는 의미 <br>
ex) ca+t
- "ct" : a가 0번 반복되어 매치x
- "cat" : a가 1번 반복되어 매치
- "caaat" : a가 3번 반복되어 매치

### 반복({m, n})
- {m} : 반드시 m번 반복 <br>
- {m ,} : m번 이상 반복 <br>
- {, n} : n번 이하 반복 <br>
- {m, n} : m번 이상, n번 이하 반복 <br>
- {?} : {0, 1} : 있어도 되고 없어도 됨 <br>

`*, +, ? 문자는 모두 {m, n} 형태로 고쳐 쓰는 것이 가능하지만 가능한 이해하기 쉽고 간결한 문자 형태로 사용하는 것이 좋다!`

## 파이썬에서 정규표현식을 지원하는 re모듈
```python
import re
p = re.compile('[a-z]+') # re.compile()을 사용하여 정규표현식을 컴파일한 결과(패턴)를 p에 저장
```
## 정규식을 사용한 문자열 검색
패턴객체를 사용하여 문자열 검색을 수행. 패턴객체는 다음과 같은 4가지 메서드 제공

|method()|목적|
|---|---|
|match()|문자열의 처음부터 정규식과 매치되는지 검색|
|search()|문자열 전체를 검색하여 정규식과 매치되는지 검색|
|findall()|정규식과 매치되는 모든 문자열(substring)을 리스트로 반환|
|finditer()|정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 반환|

### match(), search()
match () : 문자열이 처음부터 정규식과 매치될 때는 match객체를 반환, 매치되지 않을 때는 None 반환 <br>
search() : 문자열 전체 중 매치되는 문자열이 검색되면 match객체 반환, else return None
```python
# match()
>>> m = p.match("python")                   # 매치됨
>>> print(m)
<_sre.SRE_Match object at 0x01F3F9F8>       # match객체 반환

>>> m = p.match("3 python")                 # 처음부터 매치되지 않음
>>> print(m)
None                                        # None 반환

# 활용
p = re.compile('정규표현식')
m = p.match("문자열")
if m:                                       # match 될 때만 코드 실행
    ...
else :
    print("No match")

# search()
>>> m = p.search("3 python")                # 문자열 중 매치되는 부분 문자열 존재
>>> print(m)
<_sre.SRE_Match object at 0x01F3FA30>       # match 객체 반환
```

### findall(), finditer()
findall() : 문자열 중 정규식과 일치하는 부분 문자열을 리스트 형태로 반환 <br>
finditer() : 문자열 중 정규식과 일치하는 부분 문자열을 반복 가능한 객체로 반환
```python
# findall()
>>> m = p.findall("1 my 2 name 3 is 4 jisu")
>>> print(m)
['my', 'name', 'is', 'jisu']            # 문자열 중 정규식과 일치하는 부분 문자열

# finditer()
>>> m = p.finditer("1 my 2 name 3 is 4 jisu")
>>> print(m)
<callable_iterator at 0x1cf0ff75250>    # 반복 가능한 iterator 객체
>>> for mc in m : print(mc)
<re.Match object; span=(2, 4), match='my'>
<re.Match object; span=(7, 11), match='name'>
<re.Match object; span=(14, 16), match='is'>
<re.Match object; span=(19, 23), match='jisu'>    # 각각 match 객체
```

















