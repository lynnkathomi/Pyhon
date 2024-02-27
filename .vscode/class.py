class Person:
    def __init__(self,name,age):
       self.name=name ##instance variable
       self.age=age
    def greet(self):
        print(f"Hello my name is {self.name}and I'm{self.ag}years old")
person=Person ("john",78)
print(person.name)
print(person.age)
person.greet()
        


