#OOPS:

class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} eating")

    def sleep(self):
        print(f"{self.name} sleep")



class Cat(Animal):
    def __init__(self, name,is_alive, gender, year):
        super().__init__(name, is_alive)
        self.gender = gender
        self.year = year

    def jump(self):
        pass


cat = Cat("JD", True, "male", 2026)
cat.eat()
cat.sleep()