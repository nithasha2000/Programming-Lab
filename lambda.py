l = int(input("Enter the length of rectangle : "))
b = int(input("Enter the breadth of rectangle : "))
rect_area = lambda l, b: l * b #calculating area of rectangle using lambda function
print("Area of rectangle : ", rect_area(l, b))

s = int(input("Enter the side of square : "))
sq_area = lambda s: s * s #calculating area of square using lambda function
print("Area of square : ", sq_area(s))

b = int(input("Enter the base of triangle : "))
h = int(input("Enter the height of triangle : "))
tri_area = lambda b, h: (0.5) * b * h #calculating area of triangle using lambda function
print("Area of triangle : ", tri_area(b, h))
