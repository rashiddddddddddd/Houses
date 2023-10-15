# oop -> creating objects (which contins programming statments) for a small part of a bigger project
# eg: car

class employee:
    def __init__(self,name,staffno):
        self.name = name
        self.staffno = staffno
    def showDetails(self):
        print("Employee name: " + self.name )
        print("Employee no: " , self.staffno)

myStaff = []
myStaff.append(employee("Khasha Maris" , 1609))
myStaff.append(employee("Lol" , 544))

myStaff
