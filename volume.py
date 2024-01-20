#defining  the function to calculate the volume
def calculate_volume(radius, PI):
    volume = (4/3) * PI * radius**3
    return volume
#calling the function with given values of PI
PI=3.14
#prompting the user to enter the radius
radius=float(input("Enter the radius:"))
#calculating the volume
print(f"The volume of the sphere is:{calculate_volume(radius,PI)}")
