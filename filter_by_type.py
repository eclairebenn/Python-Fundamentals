def test_type(thing):
    if isinstance(thing, int):
        if thing >= 100:
            print "That's a big number!"
        elif thing < 100:
            print "That's a small number"

    if isinstance(thing, str):
        if len(thing) >= 50:
            print "Long sentence."
        elif len(thing) < 50:
            print "Short sentence."

    if isinstance(thing, list):
        if len(thing) >= 10:
            print "Big list!"
        elif len(thing) < 10:
            print "Short list."

#Testing Program 

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and i forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name', 'address', 'phone number', 'social security number']

test_type(sI)
test_type(mI)
test_type(bI)
test_type(eI)
test_type(spI)
test_type(sS)
test_type(mS)
test_type(bS)
test_type(eS)
test_type(aL)
test_type(mL)
test_type(lL)
test_type(eL)
test_type(spL)