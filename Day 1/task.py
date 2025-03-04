# Task 1 (Print somrhing)

print("\"Hello World!\"")

# Task 2(string binding)

print("Hello" + " " + "From" + " " + "India!")

# Task 3(learning input()command)

    # input("What is your name?\n")
print("Hello " + input("What is your name?\n") + "!")

# Task 4(introducing variables)

age = input("What is your age?\n")
print(age)
name = "Jack"
print(name)
name = "Paul"
print(name)
dish = input("What is your favourite dish?\n")
    # str and int cannot be added so making len(dish) a string
print("The " + dish + " has " + str(len(dish)) + " number of characters.")
    # F-string avoid string concatenation issue
print(f"The {dish} has {len(dish)} number of characters.")
