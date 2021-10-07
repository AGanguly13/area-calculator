shape = input("Please enter one of the following shapes: Triangle | Square | Rectangle : ").upper()

if shape == "TRIANGLE":
    tbase = int(input("What is the length of the base of the triangle (inches)? "))
    theight = int(input("What is the height of the triangle (inches)? "))
    tarea = 0.5*tbase*theight 
    print(f"The area of the triangle is {tarea} inches^2")

if shape == "SQUARE":
    sqside = int(input("What is the length of one side of your square (inches)? "))
    sqarea = sqside**2
    print(f"The area of the square is {sqarea} inches^2")

if shape == "RECTANGLE":
    rlength = int(input("What is the length of the rectangle (inches)? "))
    rheight = int(input("What is the height of the rectangle (inches)? "))
    rarea = rlength*rheight
    print(f"The area of the rectangle is {rarea} inches^2")
