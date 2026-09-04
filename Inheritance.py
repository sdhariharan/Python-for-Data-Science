class Animal:
    name=""
    def __init__(self,name):
        self.name=name
class Dog(Animal):

    price=0
    def __init__(self, name,price):
        super().__init__(name)
        self.price=price
    
    def display(self):
        print("Name  : ",self.name)
        print("Price : ",self.price)

a1=Dog("Puppy",5000)
a1.display()    