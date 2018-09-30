
# def num(data):
#     data = sorted(data)
#     length = len(data) /2
#     list1 = []
#     list2 = []
#     while data:
#         if not list1:
#             list1.append(data.pop())
#         if sum(list1) > sum(list2) and len(list2) < length :
#             list2.append(data.pop())
#         else:
#             if len(list1) < length :
#                 if min(data)<0:
#                     list1.append(data.pop(0))
#                 else:
#                     list1.append(data.pop())
#             else:
#                 list2.append(data.pop())
#     print('list1:',list1)
#     print('list2:', list2)
#     print('sum:', sum(list1)-sum(list2))




def num(data):
    data = sorted(data)
    print(data)
    length = len(data) /2
    list1 = []
    list2 = []
    while data:

        if not list1:
            list1.append(data.pop())
        index = 0 if min(data)<0 else -1
        if sum(list1) > sum(list2) and len(list1) <length :
            if min(data)<0 and abs(min(data)) >max(data):
                list1.append(data.pop(0))
            else:
                list2.append(data.pop())
        else:
            if len(list2) < length:
                if min(data) < 0 and abs(min(data)) > max(data):
                    list2.append(data.pop(0))
                else:
                    list1.append(data.pop())
            else:
                list1.append(data.pop())
    print('list1:',list1)
    print('list2:', list2)
    print('sum:', sum(list1)-sum(list2))

if __name__ == '__main__':
    a = [1,2,3,4,5,100]
    b = [1,2,3,4,11,12,13,14]
    c = [-5,-9,0,1,5,9]
    d = [-1,-2,-3,-4,-5,-6]
    num(c)