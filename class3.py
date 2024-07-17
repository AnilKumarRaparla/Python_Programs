class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")
class Sivaji(Animal):
    def make_sound(self):
        print("He makes more noise in class room and very good personality he has")
animal = Animal()
dog = Dog()
cat = Cat()
animal.make_sound()  
dog.make_sound()     
cat.make_sound()  

obj = Sivaji()
obj.make_sound()

'''Both super class and sub class have the same method signature
Then sub class is modify the state of the super class's method properties. 
'''