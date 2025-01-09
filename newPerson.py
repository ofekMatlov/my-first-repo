class Person:
    def __init__(self, name , age):
        self._name = name
        self ._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getPersonString(self):
        return "The name is: " + self.getName() + " The age is: " + str(self.getAge()) + " years old "

    def printMySelf(self):
        # print(self.getPersonString())
        self.getPersonString()
        
    def newCsv(self):
        new_user = {}
        new_user["Name"] = self.getName()
        new_user["Age"] = self.getAge()
        return new_user
            

