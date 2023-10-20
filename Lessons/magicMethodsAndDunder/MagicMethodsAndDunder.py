class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being denconstructed!")


p = Person("Mike", 25)

print(p.name)
print(p.age)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"




v1 = Vector(5, 5)
v2 = Vector(3, 2)
v3 = v1 + v2


print(v3.x)
print(v3.y)
print(v3)

