## 아직 진행
for cycle in range(int(input())):
    num, max_num =set(map(int,input().split()))
    double_num = num
    nums_list = []
    i = 1
    while double_num < max_num:
        double_num = num* i
        nums_list.append(double_num)
        i +=1
        
    print(f'#{cycle+1}', nums_list)
         

'''
for cycle in range(int(input())):
    num, max_num =set(map(int,input().split()))
    double_num = num
    nums_list = []
    i = 1
    while double_num < max_num:
        double_num = num* i
        nums_list.append(double_num)
        i +=1
        
    print(f'#{cycle+1}', nums_list)       
'''
# 세영이 코드 
T = int(input())
for testcase in range(1, T+1):
    start, end = map(int,input().split())
    num = start
    i = 1
    multi = []
    while num <= end:
        num = start * i
        multi.append(num)
        i+=1
    print(f'#{testcase}', end = ' ')
    print(*multi)
