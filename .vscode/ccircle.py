#from math import pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
       
    def area(self):
        PI=3.14
        area=self.radius**2*PI
        print(f"The Area of the circle is {area}")
        #return area

    def perimeter(self):
        PI=3.14
        perimeter=2*PI*self.radius
        print(f"The perimeter of the circle is {perimeter}")
rad=int(input("Enter radius"))
circle=Circle(rad) 
circle.area()  
circle.perimeter()

        
            


            


