Name = input("Enter the name: ")
subject = int(input("Enter number of subjects: "))

total = 0

for i in range(subject):
    Marks = int(input(f"Enter marks for subject {i + 1}: "))
    total += Marks

average = total / subject

print("\nName:", Name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("The rank is A")
elif average >= 80:
    print("The rank is B")
elif average >= 70:
    print("The rank is C")
elif average >= 60:
    print("The rank is D")
elif average >= 50:
    print("The rank is E")
else:
    print("Failure")