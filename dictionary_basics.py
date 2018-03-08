emilyinfo = {}
emilyinfo["Name"] = "Emily Bennett"
emilyinfo["Age"] = "21"
emilyinfo["Country of Birth"] = "United States"
emilyinfo["Favorite Language"] = "JavaScript"
emilyinfo["Favorite Color"] = "Green"

def dictionaryitems(dictset):
    for key,data in dictset.iteritems():
        print "My {} is {}".format(key, data)

dictionaryitems(emilyinfo)

newdict = {'Drink': 'Coffee', 'Nut':'Almond', "Favorite Sport":"Crew", "Favorite Team":"Seahawks"}

def keyvalue(dictset):
    for key in dictset:
        print "My {}".format(key), "is", dictset[key], "!"

keyvalue(newdict)


