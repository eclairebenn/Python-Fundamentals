import random 
def cointoss():
    headcount = 0
    tailcount = 0
    for num in range(1,5001):
        random_num = random.randint(0,1)
        if random_num == 0:
            result = "head"
            headcount += 1
        else:
            result = "tail"
            tailcount += 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(num, result, headcount, tailcount)

cointoss()
