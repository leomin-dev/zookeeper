age = int(input())

if age < 18:
    print("Minor")
elif age >= 18 and age <=64:
    print("Adult")
else:
    print("Senior")