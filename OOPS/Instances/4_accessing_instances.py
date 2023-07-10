# Accessing inside the attribute
class Backpack:

    def __init__(self):
        self.items = []
        print(self.items)

my_backpack = Backpack()


print()

# Accessing outside the attribute

class NewBackpack:

    def __init__(self):
        self.items = ["Water Bottle", "Pencils"]

my_newBackpack = NewBackpack()
print(my_newBackpack.items)

print()