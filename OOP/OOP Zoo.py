class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_Sound(self):
        print("Makes a sound")

    def printanimal(self):
        print("name:", self.name,"\n", "age:", self.age,"\n", "sound:" ,self.sound,"\n")

class Lion(Animal):
    def __init__(self, name, age, sound):
        Animal.__init__(self , name, age, sound)

    def make_Sound(self):
        print("ROAR")

class Parrot(Animal):
    def __init__(self, name, age, sound):
        Animal.__init__(self, name, age, sound)

    def make_Sound(self):
        print("Krum K R U M")

x = Lion("Kita", 12,"roar")
y = Parrot("Kurm" , 17, "mimic")

x.printanimal()
x.make_Sound()

y.printanimal()
y.make_Sound()