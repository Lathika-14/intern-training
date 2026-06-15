print("1. MULTIPLICATION TABLE")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("2.SUM 1 - 100") 
total = 0
for i in range(1, 101):
    total += i
print("Sum = ", total)   

print("3.FIZZBUZZ")
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("4.NUMBER GUESS")
target = 7
while True:
    guess = int(input("Guess the number: "))
    if guess < target:
        print("Higher")
    elif guess > target:
        print("Lower")
    else:
        print("Correct!")
        break        