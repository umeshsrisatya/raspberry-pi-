print("Division")
n = int(input("enter first number"))
m = int(input("enter second number"))
try:
    result=n/m
    print(result)
except ZeroDivisionError:
    print("please give the remainder rather than a zero")