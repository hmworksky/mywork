#1,2,100
#3,4,5
#3,2,100
#1,4,5
def jian(num1,num2):
    return num1-num2
def num(a,b):
    print(a)
    print(type(a))
    data = 0
    for i in range(len(a)):
        data = jian(a[i],b[i]+data)
        if data>=0:
            a[i],b[i] =  b[i],a[i]
            print()
        print(data)
    print('a:',a)
    print('b:', b)
    print(sum(a)-sum(b))

if __name__ == '__main__':
    data1 = [1,2,3]
    data2 = [4,5,100]
    num(data1,data2)