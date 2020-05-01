
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


    


class Cat(Mammal):
    def meaw(self):
        print("Kochi Billu")


dog1= Dog()
cat1= Cat()
dog1.walk()
dog1.bark()


cat1.walk()
cat1.meaw()

    