from re import S


class student:
    def __init__(self, name, DoB, exammark):
        self.name = name
        self.DoB = DoB
        self.exammark = exammark
        self.subjectName = []
    def displaymark(self):
        print("Student:" + self.name)
        print("Mark:" , self.exammark)

    def addsubject(self,subjectName):
        self.subjectName.append(subjectName)

    def printsub(self):
        print("subjects:" , self.subjectName)


student1 = student("Khasha",1609,55,)
student1.displaymark()
student1.addsubject("English")
student1.addsubject("Business")
student1.addsubject("Sociology")

student1.printsub()


