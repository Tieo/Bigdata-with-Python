sum([1,3,5,7], 100) # 첫 값을 100으로 쓰겠다. recursion이 가능하다. sum을 다시 넣을 수 있다. 


# 문자열

import string
string.ascii_lowercase #파이썬에서 소문자로 취급되는 애들이다. 
string.ascii_uppercase # 위와 이거 둘을 합쳐서 문자열이라고 한다. 알고리즘 문자를 풀 때, 활용하는 경우도 있고 아닌 경우도 있다. 
chr(65+1) #c를 많이해서 이런식으로 쓴다. 
ord('a')

string.digits #문자를 활용해라, 숫자를 활용해라 이럴 때 ㅏㅅ용가능하다. 

string.hexdigits
string.octdigits
string.whitespace # 공백 strip 하면 제거될 애들이다. 

'        py           ho            '.strip() # 여러 형태 공백 양 옆을 없앤다. 가운데는 못 없앴다. 여러 문자열들이 저장되어 있다. 

print('hello \'BTS\'')
print('Hello, \tWorld') # 코랩에서는 두 칸을 띄운다.
print('Hello \bWorld') #bs도 문자로 인식한다.  

oct(ord("H"))
hello_world = '\x48\x65'
print(hello_world)

print(r"\n: new line") #이스케이프 문자를 보여주고 싶을 때 사용한다.

"aaa"*"bbb"*"ccc" # 안됨

"H" in "Hello, world"

"n".lower() in "Hello, world".lower() # 대소 구분 안하는 경우에 사용한다. 
my_string = 'python'
my_string[-3] # -1 만 사용한다. 코딩할 때 헷갈린다. 판다스 같은 경우는 프로그래밍을 몇 줄 내에서 하므로 값이 이상해지거나 보기 안 좋아진다. 보여주는 관계가 간결하지 않으면 결과도 간결하지 않다. 


my_string[:3]+my_string[3:] # 머리 쓸 필요 없이 거기서 다시 시작 된다.  한 문자 뺴는 경우만 연속이 안된다. 보통 그냥 연속시키면 된다. 
my_string[:3] # 실제로는 0을 많이 빼고 쓴다. 

my_string[::2] # 두개씩 띄워서 해줘 이미지 처리에서 많이 쓴다. 


rgb = [ 122, 255, 0] # 알고리즘 문제에서는 짝수나 홀수를 참 많이 쓴다. 시작하는 값을 바꾸게 된다. 아 와우, 홀수 번쨰만 짝수번째만 고를 때 사용한다. 

my_string[::-1] # 암기 거꾸로 나온다.  마지막 값을 구할 때 많이 쓴다. 

my_str = 'aababaaaba'
my_str.capitalize()

my_str[0].upper() + my_str.lower()[1:] # upper + lower => capitalize 

my_str[:1].upper() + my_str.lower()[1:] # 확인할 수 있다. 앞글자가 다른 걸 

my_str.startswith("on") # 프로토콜이 https 냐 이런 때 많이 사용한다. 

my_str.endswith("on") 

my_str.replace(" ","") # 잘못하면 필요한 공백도 사라진다. 용도에 맞게 데이터가 어떤 의미를 가지는지 확인해서 없애는게 좋다. 


naver_complex = 'https://www.anver.com?referer=http://www.daum.com'
naver_complex.replace("http", "https", 2) # 처음부터 한 번만 실행할지 두 번 실행할지 걸정할 수 있다. 

#하나로 통일하고자 할 때, replace를 많이 사용한다. 통화나 단위를 맞추기 위해서, 

#슬라이싱 해서 하는 방법도 있다. 
"KRW" + "krw/USD"[3:]

"%".join("KRW/USD".split("/"))

my_str.center(10) #양옆을 0으로 채움

