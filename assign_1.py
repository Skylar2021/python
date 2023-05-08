# print("#3")
"""
a = 2
b = 3

a=b**a*a
a *= b**a
print(f"a: {a}")
"""
# print("#4")
# print(2**3+9-10%8)
# print("#4")
# print(7+3/(7//3))

# print("#6")
"""
num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
p = num1*num2
print(f"result: {p}") 
"""


# print("Section C#1")
"""
num = int(input("o enter a natural number1: "))
if(num <= 0):
    print("Your input is incorrect, I cannot draw a square for you!")
else:
    for i in range(1,num+1):
        for i in range(1,num+1):
            print("O", end="")
        print()
"""

# print("Section C#2")
num = int(input("enter a natural number which is greater than 3: "))
isPrime = True
r = 0
while isPrime:
    r = num
    for i in range(2, num + 1): 
        if i == 2:
            print(f"The factors of {num} are [", end="")
        if r % i == 0:
            print(f"{i}")
            print(f"b4 r = {r}")
            r = r // i
            isPrime = False
            print(f"after r = {r}")
            break


