import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    print(salaries_json)
    salaries = json.loads(salaries_json)
    print(salaries)
    salaries[name] = salary
    print(salaries)
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
print(new_salaries)
print(type(new_salaries))
decoded_salaries = json.loads(new_salaries)
print(type(decoded_salaries))
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])