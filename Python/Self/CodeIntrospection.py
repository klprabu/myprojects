# Use the help function to see what each function does.
# Delete this when you are done.
help(dir)
help(hasattr)
help(id)

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.

obj_veh = Vehicle()
obj_veh.name = "Honda"
obj_veh.color = "Red"
obj_veh.value = 30000.00
print(obj_veh.description())

print(dir(obj_veh))

# Your code goes here