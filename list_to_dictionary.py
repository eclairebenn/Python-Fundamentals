name = ["Anna", "Eli", "Pariece", "Brendan", "Amy"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# pylint: disable=print-statement
def li2di(arrkey, arrval):
    new_dict = {}
    if len(arrval) > len(arrkey):
        temparr = arrkey
        arrkey = arrval
        arrval = temparr
        for num in range(0,(len(arrkey)-len(arrval))):
            arrval.append("No value")
    
    for idx in range(0, len(arrkey)):
        new_dict[arrkey[idx]] = arrval[idx]
    return new_dict

print li2di(name, favorite_animal)