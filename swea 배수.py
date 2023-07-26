for cycle in range(int(input())):
    num, max_num =map(int,input().split()) #set쓸지 map으로 둘지 list로 둘
    double_num = 1
    nums_list = []
    i = 1
    while double_num <= max_num -num:
        double_num = num* i
        nums_list.append(double_num)
        i +=1
    print(f'#{cycle+1}', ' '.join(map(str,nums_list)))
         


