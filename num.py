import time
def num(list1,list2):
    start = time.time()
    #2个列表合并
    data = list1 + list2
    #先排序一次
    data = sorted(data)
    #获取每个列表需要填充的长度
    length = len(data) /2
    list1 = []
    list2 = []
    #先取一个最大的
    if not list1:
        list1.append(data.pop())

    #看看有没有小于0 而且绝对值大于差值的，如果有则加到大的数据列表
    index =  min(data) <0 and abs(min(data)) >= abs(sum(list1) - sum(list2))
    while data:
        #判断2个列表大小，第一次进来list1肯定大于list2，所以看看差值的判断，加上长度的校验
        if sum(list1) > sum(list2)  and len(list1) < length:
            if index:
                list1.append(data.pop(0))
            else:
                #判断列表2是否已经满足长度了
                if len(list2) == length:
                    list1.append(data.pop())
                else:
                    list2.append(data.pop())
        else:
            if len(list2) < length:
                #添加第二个列表也需要进行判断index也就是有没有小于0而且绝对值大于差值的
                if index:
                    list2.append(data.pop(0))
                else:
                    # 判断列表1是否已经满足长度了
                    if len(list1) == length:
                        list2.append(data.pop())
                    else:
                        list1.append(data.pop())
            #列表2如果满了，则向列表1中添加数据
            else:
                list1.append(data.pop())

    print('list1:',list1)
    print('list2:', list2)
    print('sum:', sum(list1)-sum(list2))
    print('time:',time.time()-start)
    return

if __name__ == '__main__':
    case_1 = list(range(10,10000))
    case_11 = list(range(1000,30000))
    num(case_1,case_11)
    # datas = a.pop(-1)
    # print(datas)
    list1 = [11,12,13]
    list2 = [1,2,3]
    num(list1,list2)

    case_2 = [-1,-2,-3]
    case_22 = [-4, -5, -6]
    num(case_2,case_22)

    case_3 = [-9, -5, -1]
    case_33 = [9, 5, 0]
    num(case_3, case_33)

    case_4 = [1, 2, 3]
    case_44 = [4, 5, 100]
    num(case_4, case_44)



