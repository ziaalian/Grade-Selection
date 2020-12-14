age = int(input("Enter your age : "))

if age < 5:
    print("You are too young")
elif age == 5:
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))
else:
    print("Go to College")