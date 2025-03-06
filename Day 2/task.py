# Task 1 (Learn primitive datatypes "Strings, integers, float, boolean")
    # Subscripting: If we want to print particular character from string we can use [i] after it.
    # Like if we want to print the first character we will write 0 as its the starting.
name = "Anushree Singh"
print(name[0])
print(name[3])
    # Easy way to print last character is starting from -1
print(name[-1])
print(name[-2])
print(name[-5] + name[10] + name[-2] + name[11])
    # String
print("123" + "456") #string concatenation
    # Integer
print(123 + 456) #here it will get added
print(123_456_789) #large num get easier to see but it will print without underscore
    # Float
print(3.14) 
    # bool
print(True)
print(False)

# Task 2 (TypeError, Checking And Conversion)

    # len(1234) can error as it doesn't support int datatype
    # Type checking:
print(type("Hello")) # If we want to check datatype of something we can use this rule
print(type(3.14))
print(type(66462838))
print(type(True))
    # Type conversion/Type Casting
print(int("123") + int("456"))
print("Number of letters in your name: " + str(len(input("Enter your name:\n"))))
    
# Task 3: Mathematical Operations

print("My age: " + str(22))
print(123)
print(12 + 34)
print(34 - 12)
print(34 * 12)
print(80 / 42)
print(80 // 42)
print(5 ** 4)
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(3 * 3 / 3 + 3 - 3)

# Exercise: BMI Calculator

height = 1.65
weight = 84

    # bmi = weight / (height * height)
bmi = weight / height ** 2

print(bmi)

# Task 4: Number Manipulation & F String

print(int(bmi))
print(round(bmi))
print(round(bmi, 2))
    # Assignment Operator: +=, -=, *=, /=
score = 0
score += 1 #user socres a point
print(score)
height = 1.8
is_winning = True
    # F-Strings
print(f"Your score is = {score}, your height is {height}, you are winning is {is_winning} ")
