"""
making a class will follow the format:
class ClassName(object):
    #attributes and methods here
"""
# pylint: disable=print-statement
class User(object):
    def __init__(self, name, email):
        #set instance variables - This method is called every time a new object is 
        #created and includes passing parameters. Do not have to pass in arguments 
        #to the self parameter. This is known as implicit passage of self.
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    
#now create instance
new_user = User("Anna", 'anna@anna.com')
print new_user.email

"""
class User(object):
    name = "Anna"
anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change: ", anna.name
bob = User()
print "bob's name : ", bob.name
"""