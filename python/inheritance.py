class Student: # Parent/Base class
    def __init__(self, n, rn): 
        self.name = n
        self.rollno = rn

    def getInfo(self):
        print(f"{self.rollno}. {self.name}")


class Exams(Student): # Child/Derived class
    def __init__(self, n, rn, s, m):
        Student.__init__(self, n, rn)
        self.subject = s
        self.marks = m

    def getPercentage(self):
        percentage = (self.marks * 100) / 50 
        print(percentage)


e1 = Exams("ABC", 1, "AI", 45)
e1.getInfo()
e1.getPercentage()