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
isNotPrime = True
r = num
while isNotPrime:
    if r == num :
        print(f"The factors of {num} are [", end="")
    elif r // i == 0:
        isNotPrime = False
        print(" ]", end="")
    else:
        print(" ,", end="")
    for i in range(2, num // 2 + 1): 
        if r % i == 0:
            print(i, end="")
            # print(f"b4 r = {r}")
            r = r // i
            break
    # if r // i == 0:
    #     isNotPrime = False
    #     print(" ]", end="")

