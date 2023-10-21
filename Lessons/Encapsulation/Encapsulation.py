class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value != "":
            self.__name = value
        else:
            self.__name = "No Name"

    @staticmethod
    def my_method():
        print("Hello Word")





p1 = Person("Eduardo", 20, 'M')
p2 = Person("",20, 'M')
p2.Name = ""

print(p1.Name)
print(p2.Name)

Person.my_method()