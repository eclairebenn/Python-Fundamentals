def type_list(list):
    newString = ""
    countStr = 0
    sumInt = 0
    countInt = 0

    for element in list:
        if isinstance(element, str):
            newString += element + " " 
            countStr += 1
        elif isinstance(element, (int, float)):
            sumInt += element
            countInt += 1

    if (countInt > 0) and (countStr > 0):
        print "The list you entered is of mixed type"
        print "String: " + newString
        print "Sum:" , sumInt
    elif (countInt > 0):
        print "The list you entered is of integer type"
        print "Sum:" , sumInt
    elif (countStr > 0):
        print "The list you entered is of string type"
        print "String: " + newString
   

x = ['magical unicorns', 19, 'hello', 98.98, 'world']
z = [2,3,1,7,4,12]
y = ['magical', 'unicorns']
type_list(x)
type_list(z)
type_list(y)

