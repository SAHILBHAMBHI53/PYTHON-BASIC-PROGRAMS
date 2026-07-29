# Swap two variables (using a third variable)

Num1 = int(input("Enter Your Number:"))
Num2 = int(input("Enter your Number:"))

print("Before Swaping Numbers")
print("Frist Number is:",Num1)
print("Second Number is:",Num2)

Temp1 = Num1                      #use temp1 Variable for Number Swap
Num1 = Num2
Num2 = Temp1

print("After Swaping Numbers")
print("Frist Number is:",Num1)
print("Second Number is:",Num2)
