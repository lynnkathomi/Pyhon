#creating a class
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area (self):
        area=self.length*self.width
        print(f"Area is {area}")
    def perimeter (self):
        perimeter=(2*self.length)+(2*self.width)
        print(f"Perimeter is {perimeter}")
len=int(input("Enter length:"))
wid=int(input("Enter width:"))
rectangle=Rectangle(len,wid)
#rectangle=Rectangle(45,3)
rectangle.area()
rectangle.perimeter()
