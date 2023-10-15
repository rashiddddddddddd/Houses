class employee:
    def __init__(self,name,staffno):
        self.__name = name
        self.__staffno = staffno
    def showDetails(self):
        print("Employee name: " + self.__name )
        print("Employee no: " , self.__staffno)

myStaff = []
while(True):
    name = input("Enter name: " )
    staffno = input("Enter num: ")

    myStaff.append(employee(name,staffno))
    option = input("0 to get out, else keep entering: ")

    if (option):
      break

for i in myStaff:
    print(i)