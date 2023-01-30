person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

#print out the name of the second child

print((person["children"])[1])

#print out the name of the cat

print ((person["pets"])["cat"])

#iterate through all children and print out each child
for i in person["children"]:
    print(i)
# print out the pets in the this format:
    #type of pet: dog name of pet: Fido
for key, value in person["pets"].items():
    print(f"type of pet: {key} name of pet: {value}")