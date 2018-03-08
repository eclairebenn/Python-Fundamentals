def findchar(list, char):
    newList = []
    for element in list:
        if char in element:
            newList.append(element)
    return newList


word_list = ['hello','world','my','name','is','Anna']
char = 'a'

print findchar(word_list, char)
