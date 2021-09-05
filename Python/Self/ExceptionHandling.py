a = (1,2,3,4,5)
print(len(a))

for i in range(20):
    try:
        print(a[i])
    except IndexError:
        print("It is out of index")
        break

print("********************************************************")

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name():
    name = actor.get("name")
    #print(name)
    last_name = name.split()[1]
    #print(last_name)
    return last_name

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
