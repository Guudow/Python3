_Author_ = "M.Guudow"

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age, name)

if age >= 18:
    print("your are old enough to vote")
    print("Please put an X in the box ")
else:
    print("Please come back in {0} years".format(18 - age))


