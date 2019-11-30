class Course:
    def __init__(self,courseName):
        self.__courseName=courseName
        self.__students=[]
    def addStudent(self,student):
        self.__students.append(student)
    def getStudents(self):
        return self.__students
    def getNumOfStu(self):
        return len(self.__students)
    def getCourseName(self):
        return self.__courseName
    def dropStudent(student):
        print("Left as an exercise")

course1=Course("History")
course2=Course("Math")
course1.addStudent("GL")
course1.addStudent("WHT")

print(course1.getNumOfStu(),course1.getStudents())
