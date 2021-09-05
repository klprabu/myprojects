import re


# Your code goes here
find_members = []
print(dir(re))
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))