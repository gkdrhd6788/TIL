def 함수():

​	return 꼭 할 필요x

함수 안에 변수명 만들고

함수() #실행시킨다음

print(변수명) 해도 비슷하다.   이건 global했을 때만 가능한듯(global안하면 not defined error 뜸)

필요시 위 방법 사용 가능

```python
# global 안했을 때
def a(x,y):
    num1=x
    num2=y

a(7,2)
print(num1)
#결과: NameError: name 'num1' is not defined

#global했을 때
num1=0  #삭제 가능

def a(x,y):
    global num1
    num1=x
    num2=y

a(7,2)
print(num1)  #7
```







함수 안에서 모든 걸 하려고 하지 말자

```python
# 변경 전
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name,age,address):
    print('현재 가입된 유저 수: ',number_of_people)
##    user_info= {}
##    user_info ['name']= name
##    user_info ['age']= age
##    user_info ['address']= address
    print(f'{name}님 환영합니다!')
    user_info = {'name': name,'age':age,'address':address}
    increase_user()
    print('현재 가입된 유저 수: ',number_of_people)
    return user_info

print(create_user('홍길동',30,'서울'))
#결과
'''
현재 가입된 유저 수:  0
홍길동님 환영합니다!
현재 가입된 유저 수:  1
{'name': '홍길동', 'age': 30, 'address': '서울'}
'''


# 변경 후
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name,age,address):
    increase_user()
    user_info = {
        'name': name,
        'age':age,
        'address':address
        }
    print(f'{name}님 환영합니다!')
    return user_info

print ('현재 가입된 유저 수: ',number_of_people)
print (create_user('홍길동',30,'서울'))
print('현재 가입된 유저 수: ', number_of_people)

#결과
'''
현재 가입된 유저 수:  0
홍길동님 환영합니다!
{'name': '홍길동', 'age': 30, 'address': '서울'}
현재 가입된 유저 수:  1
'''

```





import주의 사항

```python
# 한 파일에 두 함수가 공존 할 때( import 안쓸 때)
number_of_book = 100

def decrease_book(num_book):
    global number_of_book
    number_of_book -= num_book

def rental_book(name,num_book):
    decrease_book(num_book)
    print('남은 책의 수:',number_of_book)
    print(f'{name}님이 {num_book}권의 책을 대여하였습니다.')

rental_book('홍길동',5) 

# 결과--정답이지만, 방법이 잘못됨
'''
남은 책의 수: 97
홍길동님이 3권의 책을 대여하였습니다.
'''


# import와 비교
# 다른 파일에 book.py있음 (아래 코드)
number_of_book = 100

def decrease_book(num_book):
    global number_of_book
    number_of_book -= num_book
    return(number_of_book) 
    
# 실행 파일    
from book import number_of_book, decrease_book

def rental_book(name,num_book):
    decrease_book(num_book)
    print('남은 책의 수:',number_of_book)
    print(f'{name}님이 {num_book}권의 책을 대여하였습니다.')
    
rental_book('홍길동',3)

    
    
# 결과 --오답
'''
남은 책의 수: 100   
홍길동님이 3권의 책을 대여하였습니다.
# 이유: 함수만 가져오는 것임 .변경된 변수를 가져오는 건 아님. 따라서 number_of_book은 처음100값
'''

# import 문제점 해결책 0  --강사님이 알려주셨는데..이유는 모르겠음
import book

def rental_book(name,num_book):
    book.decrease_book(num_book)
    print('남은 책의 수:', book.number_of_book)
    print(f'{name}님이 {num_book}권의 책을 대여하였습니다.')
    
rental_book('홍길동',3)





# import 문제점 해결책1
from book import number_of_book, decrease_book


def rental_book(name,num_book):
    left = decrease_book(num_book) #변수를 하나 받아옴
    print('남은 책의 수:',left)
    print(f'{name}님이 {num_book}권의 책을 대여하였습니다.')
    

rental_book('홍길동',3)

# 결과(정답)
'''
남은 책의 수 97
홍길동님이 3권의 책을 대여하였습니다.
'''





# import 문제점 해결책2--사실 이게 문제의 의도
# 다른 파일에 book.py있음 (아래 코드)--print문을 여기서 돌린다.(독립적
number_of_book = 100

def decrease_book(num_book):
    global number_of_book
    number_of_book -= num_book
    print('남은 책의 수',number_of_book)
    
# 실행 파일  
from book import number_of_book, decrease_book


def rental_book(name,num_book):
    decrease_book(num_book)  #요렇게 독립적으로
    print(f'{name}님이 {num_book}권의 책을 대여하였습니다.')
    

rental_book('홍길동',3)

# 결과(정답)
'''
남은 책의 수 97
홍길동님이 3권의 책을 대여하였습니다.
'''


```

질문

```python
a=0

def my_func():
    global a
    a += 1

def test(a):
    print(a)
    my_func()
    print(a)
 
test(a) # 왜 안바뀌지??위에 increse 함수와 다르네?
```

