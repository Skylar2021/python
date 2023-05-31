# import random

# for i in range(1,8):
#     print(random.randint(1,49), "","",sep=" ",end="")


# num1 = random.randint(1,49)
# num2 = random.randint(1,49)
# num3 = random.randint(1,49)
# num4 = random.randint(1,49)
# num5 = random.randint(1,49)
# num6 = random.randint(1,49)
# num7 = random.randint(1,49)

# print(
#     num1,
#     num2,
#     num3,
#     num4,
#     num5,
#     num6,
#     num7,
#       )

# age = 18

# def demo(name, age = 18, gender = "unknown"):
#     age = age + 1
#     print("name",name)
#     print("age",age)
#     print("gender",gender)
# demo("Skylar", gender = "F", age=20)

# def trytry( *agrs, **kwargs):
#     for i in agrs:
#         print(type(i),i)
#     for key in kwargs:        
#         print("key",key)
#         print("kwargs[key]",kwargs[key])
#         print("type(kwargs[key])",type(kwargs[key]))

# trytry(1.0,2,"str",one=1,true=True)

# test = {"key": "value"}
# print(test['key'])

# import sys
# print("sys.argv", sys.argv)
# for i in sys.argv:
#     print("i", i)

numList = [1,'2',3]

print(sum(numList))