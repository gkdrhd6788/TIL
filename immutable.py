#알고리즘에서 나옴
#아까 질문한것과 관련있나?
#int로 해보자

#
def func(num):
    num[0] = -1  #mutable은 global없이 읽기,수정가능 (수정하는 단계가 다름-중간단계)
    print(num)


num =[1,2,3]
func(num)
print(num)



#
def func():
    num[0] = -1
    print(num)


num =[1,2,3]
func()
print(num)






#
def func():
    num = [1,2,3]
    print(num)

num= [1,2,3]
func ()
print(num)


#
def func():
    global num = [1,2,3]
    print(num)

num= [1,2,3]
func ()
print(num)
