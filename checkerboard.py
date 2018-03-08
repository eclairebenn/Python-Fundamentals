# pylint: disable=print-statement
def checkerboard(height, width):
    check = ""
    for num in range(0,height):
        if num % 2 == 0:
            for square in range(0,width):
                check += "* "
            print check
            check = ""
        if num % 2 != 0:
            for square in range(0,width):
                check += " *"
            print check
            check = ""
checkerboard(11, 11)
    
    
