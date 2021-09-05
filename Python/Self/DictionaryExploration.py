val = {
    "Prabu"     : "0173716940",
    "Maya"      : "0182618502",
    "Sidharth"  : "0726452193",
    "Samarth"   : "0243432234"
}

print(type(val))

for i,j in val.items():
    print(i,j)

## New example

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

phonebook["Jake"] = 938273443
phonebook.pop("Jill")

print(phonebook)
# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


print(phonebook.get("Jake"))