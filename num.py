
def num(data):
    data = sorted(data)
    length = len(data) /2
    list1 = []
    list2 = []
    while data:
        if sum(list1) > sum(list2) and len(list2) < length:
            list2.append(data.pop())
        else:
            if len(list1) < length:
                list1.append(data.pop())
            else:
                list2.append(data.pop())


if __name__ == '__main__':
    a = [1,2,3,4,5,100]
    b = [1,2,3,4,11,12,13,14]
    print(sorted(a))
    num(b)