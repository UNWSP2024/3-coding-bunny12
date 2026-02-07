# Name: Abrielle Nyei
# Program: Age Classifier
# Date: February 6, 2026

age = int(input("Enter the person's age: "))

if age <= 1:
    print("Infant")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
