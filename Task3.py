import random

a = random.randint(1,10)
b = random.randint(1,10)
action_list = ["+", "-", "*", "//"]
action = action_list[random.randint(0,3)]

if action == "+":
    result = a + b
elif action == "-":
    result = a - b
elif action == "*":
    result = a * b
elif action == "//":
    result = a // b

print(a, action, b, "=")


c = input()
if int(c) == result:
    print("correct")
else:
    print("try again")
