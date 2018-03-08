def multtable():
    startArr = ["x",1,2,3,4,5,6,7,8,9,10,11,12]
    arr = []
    print startArr
    for num in range(1,13):
        arr.append(num)
        for mult in range(1,len(startArr)):
            arr.append(num*mult)
        print arr
        arr = []
multtable()