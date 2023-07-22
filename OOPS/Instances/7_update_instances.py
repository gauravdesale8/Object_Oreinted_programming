class Backpack:

    def __init__(self, color):
        self.items = []
        self.color = color


my_color = Backpack("Blue")
your_color = Backpack("Red")

print(my_color.color)
print(your_color.color)

print("Changing the color:")
my_color.color = "Green"

print(my_color.color)
print(your_color.color)