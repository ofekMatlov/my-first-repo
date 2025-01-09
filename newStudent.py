from newPerson import Person
import utilities

class Student(Person):
    def __init__(self,name, age):
        super().__init__(name, age)
        
        self.field_of_study = input("Please Enter field of study: ")
        self.year_of_study = input("Please Enter year of study: ")
        self.score_avg = input("Please Enter score avg: ")
        
        if utilities.digitisok(self.year_of_study) == False:
            return -1
        elif utilities.digitisok(self.score_avg) == False:
            return -1

    def getFieldOfStudy(self):
        return self.field_of_study

    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg  

    def printStudent(self):
        print(self.getPersonString() + ", The field of study is: " + self.getFieldOfStudy() + " The year of study is: " + str(self.getYearOfStudy()) + " The score avg is: " + str(self.getScoreAvg()))

    def printMySelf(self):
        self.printStudent()

    def newCsv(self):
        new_user =  super().newCsv()
        new_user["field of study"] = self.getFieldOfStudy()
        new_user["Year of study"] = self.getYearOfStudy()     
        new_user["Score avg"] = self.getScoreAvg()
        return new_user
    




        
