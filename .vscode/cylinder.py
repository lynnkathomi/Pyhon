def cylinder_function(RADIUS, HEIGHT):
    PI = 3.14  # Assign the value of PI here
    area = PI * RADIUS**2 * HEIGHT
    print("The area of a cylinder:", area)

RADIUS = float(input("Enter radius:"))
HEIGHT = float(input("Enter height:"))
cylinder_function(RADIUS, HEIGHT)  # Call the function with correct arguments

