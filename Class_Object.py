class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    
    @id.setter
    def id(self,id):
        self.__id=id
        
    @name.setter
    def name(self,name):
        self.__name=name;
        
    def display(self):
        print("ID   :", self.id)
        print("Name :", self.name)


s1 = Student(1, "Hariharan")
s2 = Student(2, "Krethikesh")
print(s1.name)
s1.display()
s2.display()