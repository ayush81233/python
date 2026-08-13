num = int(input("Enter the number: "))
total= 0

while num >0:
    digit = num%10
    total = total +digit
    num = num//10
    
print("the sum of the digit is : ", total )