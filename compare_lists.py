def compare(list1, list2):

    if len(list1) != len(list2):
        print "The lists are not the same"
    else:
        for idx in range(len(list1)):
            if list1[idx] != list2[idx]:
                print "The lists are not the same"
                return False       
            else:
                continue
        print "The lists are the same!"

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

compare(list_one, list_two)

    
            