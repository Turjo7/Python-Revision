class Person:


    def __init__(self,name):
        super().__init__()
        self.name=name
        print(name)

    def talk(self):
        print(f''' Hi, I am {self.name}''')




turjo = Person("Turjo")
turjo.talk()
print(turjo.name)


billu = Person("Billu")
billu.talk()
print(billu.name)