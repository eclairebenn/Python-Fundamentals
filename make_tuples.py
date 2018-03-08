
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dicttotuple(dictInput):
    key = ""
    value = ""
    returntuple = []
    for k in dictInput:
        key = k
        value = dictInput[k]
        returntuple.append((key, value))
    print returntuple

dicttotuple(my_dict)