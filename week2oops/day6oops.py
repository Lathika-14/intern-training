print("1.STUDENT CLASS")
class Student:
    def __init__(self, name, grade):                
        self.name = name
        self.grade = grade
    def study(self):
        print(self.name, "is studying")
    def play(self):
        print(self.name, "is playing")
name = input("Enter student name: ")
grade = input("Enter student grade: ")
student1 = Student(name, grade)
print("Name:", student1.name)
print("Grade:", student1.grade)
student1.study()
name = input("Enter student name: ")
grade = input("Enter student grade: ")
student2 = Student(name, grade)
print("Name:", student2.name)
print("Grade:", student2.grade)
student2.play()


print("2.BANK ACCOUNT")
class BankAccount:
    def __init__(self, balance): 
        self.balance = balance    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")
balance1 = float(input("Enter Account 1 starting balance: "))
account1 = BankAccount(balance1)
deposit1 = float(input("Enter Account 1 deposit amount: "))
account1.deposit(deposit1)
withdraw1 = float (input("Enter Account 1 withdrawal amount: "))
account1.withdraw(withdraw1)
print()
balance2 = float(input("Enter Account 2 starting balance: "))
account2 = BankAccount(balance2)
deposit2 = float(input("Enter Account 2 deposit amount: "))
account2.deposit(deposit2)
withdraw2 = float(input("Enter Account 2 withdrawal amount: "))
account2.withdraw(withdraw2)