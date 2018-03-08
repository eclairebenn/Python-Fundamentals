students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def exportinfo1(inputList):
    for idx in range(0,len(inputList)):
        print "\n"
        for key in inputList[idx]:
            print inputList[idx][key],

#exportinfo1(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def exportinfo2(inputDict):
    tempname = ""
    lengthname = ""
    for key in inputDict:
        print key         
        for idx in range(0,len(inputDict[key])):
            for val in inputDict[key][idx].itervalues():
                tempname += val + " "
            lengthname = len(tempname)-2
            print idx, " - ", tempname, " - ", lengthname
            tempname = ""
                       
exportinfo2(users)


