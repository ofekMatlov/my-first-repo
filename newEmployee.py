from newPerson import Person
import utilities
class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        
        self._field_of_work = input("Please Enter field of work: ") 
        self._salary = input("Please Enter salary: ")

        if utilities.digitisok(self._salary) == False:
            return -1
        
    def getFieldOfWork(self):
        return self._field_of_work 
    
    def getSalary(self):
        return self._salary

    def printEmployee(self):
         print(self.getPersonString() + ", The field of work is, " + self.getFieldOfWork() + " The salary is, " + str(self.getSalary()))
    
    def printMySelf(self):
        self.printEmployee()
       #    print(self.printEmployee())

    def newCsv(self):
        new_user=  super().newCsv()
        new_user["Salary"] = self.getSalary()
        new_user["Field of work"] = self.getFieldOfWork()
        return new_user    

