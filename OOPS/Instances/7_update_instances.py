class Backpack:

    def __init__(self, color):
        self.items = []
        self.color = color


my_color = Backpack("Blue")
print(my_color.color)

print("After changing the value:")
my_color.color = "Green"

print(my_color.color)
