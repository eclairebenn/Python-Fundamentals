def oddeven():
    for num in range(1,2001):
        if num % 2 == 0:
            print "Number is {}. This is an even number.".format(num)
        else:
            print "Number is {}. This is an odd number.".format(num)

#oddeven()

def multiply(arr, m):
    for val in range(0,len(arr)):
        arr[val] *= m
    return arr
a = [2,4,10,16]
#print multiply(a, 5)

def layered_multiples(arr):
    newArr = []
    tempArr = []
    for value in arr:
        tempArr += value * [1]
        newArr.append(tempArr)
        tempArr = []
    return newArr

x = layered_multiples(multiply([2,4,5],2))
print x