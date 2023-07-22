class Backpack:

    def __init__(self, color, size):
        self.color = color
        self.size = size


my_color = Backpack("Blue", 6)
your_color = Backpack("Red", 2)

my_and_your_col = [my_color, your_color]

for colors in my_and_your_col:
    print(colors.color)
    print(colors.size)