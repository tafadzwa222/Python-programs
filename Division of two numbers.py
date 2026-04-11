#Python program to find the division of two numbers
a=float(input("Enter a value: "))
b=float(input("Enter b value: "))
div=a/b
if b==0:
    print("The divison process is not possible!")
else:    
 print("Th edivison result of {} and {} is: {}".format(a,b,div))
