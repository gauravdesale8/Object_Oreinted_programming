class Circle:

    def __init__(self, radius=5):
        self.radius = radius

print("")
print("<><><><><><><><><><><><><>")
print("Printing default argument:")
my_radius = Circle()
print(my_radius.radius)
print("<><><><><><><><><><><><><>")

print("")

print("<><><><><><><><><><><><><>")
print("Printing explicit argument(no default argument):")
my_radius = Circle(8)
print(my_radius.radius)
print("<><><><><><><><><><><><><>")
print("")