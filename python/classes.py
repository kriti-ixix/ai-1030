class Student:
    def __init__(self, rn, n, s, m): # Constructor
        print("Welcome to this school!")
        self.rollno = rn
        self.name = n
        self.subject = s
        self.marks = m

    def calculatePercentage(self):
        pass

    def __str__(self):
        return f"{self.rollno}. {self.name} -> {self.subject}"

s1 = Student(5, 'ABC', 'Web', 56)
print(s1)

s2 = Student(1, 'XYZ', 'AI', 50)
print(s2)

s3 = Student(3, 'PQR', 'Data Science', 45)
print(s3)