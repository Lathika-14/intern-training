print("1.NUMBER CLASSIFIER")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("2.GRADE CALCULATOR")
score = int(input("Enter score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

print("3.LOGIN CHECK")
stored_password = "python258"
username=input("enter a username:")
password = input("Enter password: ")
if password == stored_password:
    print("Login Successful")
else:
    print("Invalid Password")

print("4.LARGEST OF THREE NOS")
a = (input("A: "))
b = (input("B: "))
c = (input("C: "))
if a >= b and a >= c:
    print("A Largest:", a)
elif b >= a and b >= c:
    print("B Largest:", b)
else:
    print("C Largest:", c)    