name = input("Enter student name: ")

maths = int(input("Enter Maths mark: "))
science = int(input("Enter Science mark: "))
computer = int(input("Enter Computer mark: "))

total = maths + science + computer
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")