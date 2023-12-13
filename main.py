# main.py
from shape_calculator import Rectangle, Square

def get_user_input():
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    return width, height

# Create a Rectangle based on user input
rect_width, rect_height = get_user_input()
rect = Rectangle(rect_width, rect_height)

# Display information about the Rectangle
print(f"\nRectangle created: {rect}")
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")
print(f"Diagonal: {rect.get_diagonal()}")
print(f"Picture:\n{rect.get_picture()}")

# Create a Square based on user input
side_length = float(input("\nEnter side length for the square: "))
sq = Square(side_length)

# Display information about the Square
print(f"\nSquare created: {sq}")
print(f"Area: {sq.get_area()}")
print(f"Diagonal: {sq.get_diagonal()}")
print(f"Picture:\n{sq.get_picture()}")

# Check how many times the Square can fit inside the Rectangle
print("\nChecking how many times the square can fit inside the rectangle:")
print(f"Number of times: {rect.get_amount_inside(sq)}")
