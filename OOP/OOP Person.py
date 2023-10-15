


class person:
    def __init__(self,fn,ln,age):
        self.__fn = fn
        self.__ln = ln
        self.__age = age

    def save_to_file(self,filename):
        file = open(filename,"a")
        data = input("enter text you want to append: ")
        file.write(data + "\n")
        file.close()

    def load_from_file(self,filename):
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()

    def blank(self,filename):
        file = open(filename, "r")
        file.truncate(99)
        file.close()

    
class classroom:
    def __init__(self,Students):
        self.__students = [Students]

    def addStudent(self,Students):
        self.__students.append(Students)

    def showdetails(self):
        print("classroom: " , self.__students)

person1 = person("khasha","maris",18)

person1.save_to_file("Khasha")
person1.load_from_file("Khasha")

# classroomroster = classroom("Khasha")

# for i in range(2):
#     Students = input("enter name: ")
#     classroomroster.addStudent(Students)

# classroomroster.showdetails()
