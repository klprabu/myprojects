# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# Code starts here

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.value = 60000.00
car1.color = "red convertible"

car2.name = "Jump"
car2.value = 10000.00
car2.color = "blue van"

# test code
print(car1.description())
print(car2.description())