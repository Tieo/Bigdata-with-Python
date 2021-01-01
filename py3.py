my_str = "aaabbbccc"

"".join(set([c for c in my_str]))

set([c for c in my_str])

list([c for c in my_str])


my_list = list((1,3,5,7,9)) #다른 자료구조형에서 가져올 때 사용한다. 리스트를 주로 보기 때문에 리스트 정의와 초기화를 한다. 리스트도 문자열과 같이 연산자가 있다. 

[1,3,5] + [7,9] #문자열과 비슷

#곱셈은 반복할 때, 리스트 원소가 하나일 때, 콤마로 확실히 표현 가능하다. 
[0, ]*3

([1,3,5]+[7,9]) == my_list

#set은 위험하다, 값이 사라진다. 

#리스트의 길이 , 크기, len
len(my_list)

#크기보다 하나 작은 애를 해줘야 마지막 애를 가져올 수 있다. 인덱싱 할 때 값을 하나 작게 해야 한다. 누구나 많이 하는 실수이다. 문제가 있다고 알아 채는게 중요하다.


my_list[len(my_list)-1] #이건 그냥 [-1]

#넘어가면 에러가 난다. 코딩테스트에서 꼭 검사하는 요건 중 하나이다. 첫번째 값, n번째 값, 그리고 마지막 값, 마지막 +1 값을 먼저 검사한다. 
#제출하면 한번만 검사해서 끝나는게 아니라, 평균을 낸다. 메모리를 얼마나 썼는지 본다. 일단 for 문이나 if 문에 위 값들을 먼저 대입한다. 1,2,3번째 값까지 예외 처리를 해주어야 한다. 

#0을 생략하는게 대부분 낫다.
my_list[::2]

# 슬라이싱은 복사해서 쓰는데, 
my_list3 = my_list[:]
my_list4 = my_list[:]

my_list2 = my_list # 이건 복제가 아니다. 그래서 reference라고 한다. 복제가 아니다. 


my_list = [1,2,3,4,5,6,7,8,9,10]

my_list[::2]

my_list[1::2]

my_list[:-1]

my_list[::-1]

my_list = [int(c) for c in my_str]

my_list[::-1][0]

my_list.copy()
my_list[:] # 슬라이싱 써라 그냥


my_list = []

my_list.append([2,3])
my_list.extend([2,3])
my_list + [2,3] # extend와 같은 개념이다. extend는 알아만 두고 간편한 거 쓰면 된다. 

my_list2 = my_list[:]
my_list2.clear()

my_list2 = my_list[:]
my_list2.remove(2) # 하나씩 없애면 된다. 

my_list2 = my_list[:]
my_list2.sort(reverse=True) # 원본도 변해버린다. 
sorted(my_list) # 새로운 리스트를 만들어서 결과를 내뱉고 원본은 변하지 않는다. 

my_list2 = my_list[:]
my_list
my_list2.reverse()
my_list2
my_list3 = my_list[:]
reversed(my_list3) #이터레이터이다. 리스트로 보고 싶으면 리스트를 씌워준다. 
list(reversed(my_list3))
my_list[::-1]

my_dict = {}
my_dict['f'] = 60

my_dict.get('z') # 없으면 None을 반환한다. 

my_dict.get('z', 2)

del my_dict['f']
'a' in my_dict

my_dict.keys()
list(my_dict.keys())
my_dict['a']
my_dict['b'] # 이 두개를 가져오는 속도가 같다. 배열은 0이 더 빠르다. 딕트는 읽는 속도가 같다. 딕트 키즈라고 되어 있다. 

my_dict.values()
list(my_dict.values())
#키와 값을 따로 가져오는 방법은 items
list(my_dict.items())

# dict 값 변경하기 
my_dict[key] = value
my_dict.update({"key":"value"})
#업데이트 위험하다. 살아있으면 어디가 잘못되는지 모른다. 죽으면 죽어서 위험하고, 살면 어딨는지 몰라서 위험하다. 

#얘는 복제가 답이 없다. copy() 써야한다. 그냥 대입하면 값을 넣으면 값이 변경 된다. 
