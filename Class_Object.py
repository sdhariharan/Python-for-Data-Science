class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print("ID   :", self.id)
        print("Name :", self.name)


s1 = Student(1, "Hariharan")
s2 = Student(2, "Krethikesh")

s1.display()
s2.display()