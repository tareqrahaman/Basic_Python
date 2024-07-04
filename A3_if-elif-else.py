#taking user input
num = int(input("Enter an integer number: "))

#handling task1
print("\n____Task1____")
if num>0: 
    print(f"{num} is positive.")
elif num<0:
    print(f"{num} is negative.")
else: 
    print(f"{num} is zero.")
print()

#handling task2
print("__Task2__")
if num%2==0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
print()

#handling task3
print("__Task3__")
if num>100 or num<0:
    print("Invalid value.")
elif num>=90:
    print("Grade: A")
elif num>=80:
    print("Grade: B")
elif num>=70:
    print("Grade: C")
elif num>=60:
    print("Grade: D")
else:
    print("Grade: F")
print()