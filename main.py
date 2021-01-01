'''변수 ' _ ' 
_ 225는 어떤 수냐면, 위에 있는 수와 같다. print 안 찍은 것과 같이 생산성을 높이기 위해서 변수 언더바를 정의해주는데, 마지막에 실행된 값을 항상 가지고 있다. 
'''
#round? #colab 에서 설명을 볼 수 있다. 
help(round) # 설명을 볼 수 있다. 
_= 2
round(_, 2) # help는 숫자와 직접적이진 않은데 도움이 된다. 
my_list = []
#변수에 넘기는 수가 있다. 
my_list = [3,5,7] # 이게 비어있으면 에러가 뜬다. 그럼 default를 지정해준다. 누락된 값을 처리할 때, 리스트가 비어있는 경우. 
min(my_list)

min(my_list, default=100)
max([4,5,7])
max(4,5,7) # 흔한 경우는 아님
max([], default=3)

# 나중에 이부분을 많이 활용해서 쓴다. 
#lambda x:x['age'] 는 def get_age(x): return x['age'] 이다. 그래서 매번 이렇게 함수 정의를 두줄로 쓰는데, 함수를 한 줄로 만들겠음이라는 뜻이다.

#2진수, 8진수, 10진수, 16진수 -bin -oct -int -hex

[i for i in bin(75)]

[i for i in bin(75)[2:]]

#divmod(a,b) a는 피제수 b는 제수

#암호화할 때도 많이 쓴다. 한꺼번에 
divmod(17,3)

a,b = divmod(17,3 ) # 두개를 따로 받아올 수 있다. 
#나머지만 쓸거다라면
_, b = divmod(17,3)

pow(3,2) % 7 #이걸 많이 써서 
pow(3,2,7)

complex(3, 4) # 복소수 

# 기본연산 끝

