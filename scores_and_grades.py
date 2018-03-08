import random 

def score_and_grade():
    print "Scores and Grades"
    for num in range(0,10):
        random_num = random.randint(60,101)
        if random_num < 70:
            print "Score : {}; Your grade is D".format(random_num)
        if random_num >=70 and random_num < 80:
            print "Score : {}; Your grade is C".format(random_num)
        if random_num >= 80 and random_num < 90:
            print "Score : {}; Your grade is B".format(random_num)
        if random_num >= 90:
            print "Score : {}; Your grade is A".format(random_num)
    print "End of the program. Bye!"

score_and_grade()